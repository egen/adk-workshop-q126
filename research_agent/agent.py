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
# root_agent = Agent(
#     name="...",
#     model="...",
#     instruction="...",
#     description="...",
# )

root_agent = Agent(
    name="Recipe_Researcher",
    model="gemini-2.0-flash",
    instruction="""You are a recipe research assistant that helps users find information about recipes. 
    You haveaccess to a google search tool that you can use to find information on the web.
    When a user asks you a question, you should first try to answer it based on your existing knowledge. If you don't know the answer, or if you think you can find a better answer by searching the web, you should use the google search tool to find the information. 
    After using the google search tool, you should use the information you found to answer the user's question.""",
    description="An agent specialized in helping with research tasks.",
    tools=[google_search]
)