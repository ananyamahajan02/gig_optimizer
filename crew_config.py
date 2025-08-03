import os
import litellm
from dotenv import load_dotenv
from crewai import Agent, Task, Crew

load_dotenv()

os.environ["LITELLM_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LITELLM_LOG"] = "DEBUG"


litellm.set_verbose = True
llm_model = "openrouter/mistralai/mistral-7b-instruct:free"


def create_crew(freelancer_profile: str):
    # Agent 1: Profile Analyzer
    analyzer = Agent(
        role="Profile Analyzer",
        goal="Find weaknesses and missing elements in a freelancer profile.",
        backstory="An expert in analyzing Upwork and Fiverr gigs.",
    )

    # Agent 2: Niche Researcher
    researcher = Agent(
        role="Niche Researcher",
        goal="Suggest trending and profitable niches for freelancers.",
        backstory="Tracks freelance markets and high-demand skills constantly.",
    )

    # Agent 3: Gig Writer
    writer = Agent(
        role="Gig Writer",
        goal="Write compelling gig titles and descriptions for freelancing platforms.",
        backstory="Crafts optimized gigs that increase conversions and profile views.",
    )

    # Tasks
    task1 = Task(
        description=f"Analyze this freelancer profile and point out issues:\n\n{freelancer_profile}",
        expected_output="List of weaknesses or missing elements.",
        agent=analyzer,
    )

    task2 = Task(
        description="Based on the issues found above, suggest 3 trending gig niches relevant to the freelancer's background.",
        expected_output="Three high-demand niche suggestions with reasoning.",
        agent=researcher,
    )

    task3 = Task(
        description="Using the profile analysis and niche suggestions, write an optimized Fiverr gig title and description.",
        expected_output="1 gig title and 1 compelling description.",
        agent=writer,
    )

    # Create and return Crew
    return Crew(
        agents=[analyzer, researcher, writer],
        tasks=[task1, task2, task3],
        verbose=True,
    )