"""
ADK Workshop - Research Agent

This is your starting point for the workshop exercises.
Follow the instructions in the README to progressively build
your Research Agent from a simple single agent to a full
multi-agent system.

Current Exercise: 1 (Simple Single Agent)
"""

from google.adk.agents import Agent
from google.adk.tools import google_search

# Exercise 1: Create a simple research agent
# TODO: Define your root_agent here
#
# Hints:
# - Use the Agent class from google.adk.agents
# - Set a descriptive name, model, instruction, and description
# - The model should be "gemini-2.0-flash" for fast responses
#
# Example structure:
root_agent = Agent(
    name="research_agent",
    model="gemini-2.0-flash",
    instruction="""
    You are a research agent that helps users find information.
    When given a query, use the Google Search tool to find relevant information.
    Always provide concise and accurate answers based on the search results.
    """,
    description="An agent specialized in conducting research and providing insights.",
    tools=[
        google_search
        ]
)

root_agent = root_agent  # Replace this with your Agent definition
