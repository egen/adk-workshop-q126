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

# root_agent = None  # Replace this with your Agent definition

root_agent = Agent(
    name="simple_research_agent",
    model="gemini-2.0-flash",
    instruction="""
    You are a helpful research assistant. Your goal is to help user's find information and answer questions.

    You have access to a fetch_webpage tool that allows you to read the content of web pages.Use this to collect more information before responding to the user.
    """,
    description="""
    This is a simple research agent that can answer questions and find information for the user.
    """,
    tools=[fetch_webpage]
)