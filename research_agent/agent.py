from google.adk.agents import Agent

from .tools import fetch_webpage

root_agent = Agent(
    name="research_agent",
    model="gemini-2.0-flash",
    description="A research assistant that can fetch and read web pages to help answer questions.",
    instruction="""You are a research assistant with the ability to fetch and read web pages.""",
    tools=[fetch_webpage],
)
