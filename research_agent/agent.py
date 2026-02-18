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
from .tools import fetch_webpage



# Exercise 1: Create a simple research agent
# TODO: Define your root_agent here
#
# Hints:
# - Use the Agent class from google.adk.agents
# - Set a descriptive name, model, instruction, and description
# - The model should be "gemini-2.0-flash" for fast responses
#
# Example structure:
# root_agent = Agent(
#     name="...",
#     model="...",
#     instruction="...",
#     description="...",
# )

root_agent = Agent(
    name="research_assistant",
    model="gemini-3-flash",
    instruction="""
    You are a helpful research assistant. Your goal is  to Answer questions and provide information based on your knowledge.
    Remember: You have access to the google_search tool to query information from the web and verify the information before providing it.
    You also have access to the fetch_webpage tool to read the content of specific webpages.
    """,
    description="A simple research agent that can answer questions and provide information.",
    tools=[google_search, fetch_webpage]
)  
