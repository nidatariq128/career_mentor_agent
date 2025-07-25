from agents import Agent, RunConfig, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from dotenv import load_dotenv
from roadmap_tool import get_career_roadmap
import os

load_dotenv()
api_key = os.getenv("GEMINI_API_KYE")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Define the agents
career_agent = Agent(
    name="CareerAgent",
    instructions="You are a career mentor agent. Provide career advice and roadmaps based on user queries.",
    model=model
)

skill_agent = Agent(
    name="SkillAgent",
    instructions="You are a skill mentor agent. Provide skill development advice using the get_career_roadmap tool.",
    model=model,
    tools=[get_career_roadmap]
)

job_agent = Agent(
    name="JobAgent",
    instructions="You are a job mentor agent. Provide job search advice based on the user’s career field.",
    model=model
)

# Main flow
def main():
    print("\n🎓 Career Mentor Agent\n")

    interest = input("What career are you interested in?").strip()

    result1 = Runner.run_sync(career_agent, interest, run_config=config)
    field = result1.final_output.strip()
    print("\n📌 Suggested Career Field:", field)

    result2 = Runner.run_sync(skill_agent, field, run_config=config)
    print("\n📚 Suggested Skills and Roadmap:", result2.final_output)

    result3 = Runner.run_sync(job_agent, field, run_config=config)
    print("\n💼 Job Search Advice:", result3.final_output)

    again = input("\nDo you want to explore another career? (yes/no): ").strip().lower()
    if again == "yes":
        main()
    else:
        print("\nThank you for using the Career Mentor Agent! Goodbye! 👋")

# Entry point
if __name__ == "__main__":
    main()