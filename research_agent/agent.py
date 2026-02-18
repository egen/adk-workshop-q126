"""
ADK Workshop - Research Agent

This is your starting point for the workshop exercises.
Follow the instructions in the README to progressively build
your Research Agent from a simple single agent to a full
multi-agent system.

Current Exercise: 1 (Simple Single Agent)
"""

from google.adk.agents import Agent
from google.adk.tools import google_search  # Importing the Google Search tool from the ADK tools module

root_agent = Agent(
    name="simple_research_agent",
    model="gemini-2.0-flash",
    instruction="""You are a helpful research assistant. Your task is to 
    help users find information and answer questions by gathering relevant
    data and providing concise summaries.
    You have access to a web search tool that allows you to perform Google searches
    to find information on the internet.""",
    description="A simple research agent",
    tools=[
        google_search,  # This tool is defined in tools.py and allows the agent to perform web searches
    ]
)
