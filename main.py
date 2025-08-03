from crew_config import create_crew
if __name__ == "__main__":
    with open("profile_input.txt", "r") as f:
        profile = f.read()
    
    crew = create_crew(profile)
    
    print("🔁 Running Freelancer Gig Optimizer...")
    result = crew.kickoff()
    print("\n✅ Final Result:\n")
    print(result)
