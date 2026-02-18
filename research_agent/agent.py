
"""
ADK Workshop - Research Agent

This is your starting point for the workshop exercises.
Follow the instructions in the README to progressively build
your Research Agent from a simple single agent to a full
multi-agent system.

Current Exercise: 1 (Simple Single Agent)
"""

from google.adk.agents import Agent
#from google.adk.tools import google_search
from .tools import fetch_webpage

root_agent = Agent(
    name="research_agent",
    model="gemini-2.0-flash",
    description="A research assistant that helps users find and understand information.",
    instruction="""You are a helpful research assistant. Your goal is to help users to 
    find information and answer their questions clearly and accurately.

    You have access to google search tool to find and verify information before presenting it to the user.
    Always use the tool when you need to find information or verify facts.
    Speak to me like Liam Neeson in Taken, but be helpful and informative. Always be concise and to the point.
    """,
    tools=[
        fetch_webpage
    ]
)
