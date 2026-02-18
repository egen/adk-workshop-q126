
from google.adk.agents import Agent
from google.adk.tools import google_search_tool

root_agent = Agent(
name="snigdha_research_agent",
model="gemini-2.0-flash",
description="A research assistant that helps users find and understand information.",
instruction="""You are a helpful research assistant. Your goal is to help users
find information and answer their questions clearly and accurately.

Remember: In this version, you have access to the Google Search tool to help find information before 
presenting any response to the user.
"""
tools=[google_search_tool]
)