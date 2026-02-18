"""
ADK Workshop - Research Agent

This is your starting point for the workshop exercises.
Follow the instructions in the README to progressively build
your Research Agent from a simple single agent to a full
multi-agent system.

Current Exercise: 1 (Simple Single Agent)
"""

from google.adk.agents import Agent
# from google.adk.tools import google_search -exercise-2
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

    # ex-2->Remember: In this version you do not have access to any tools and
    # all information must come from your training knowledge.
    # """,
    # You have access to a fetch_webpage tool, use this to collect
    # more information about the topic before responding to the user.
root_agent = Agent(
    name="basic_research_agent_tool",
    model="gemini-2.0-flash",
    instruction="""
   You are a helpful research assistant. Your goal is to help users
    find information and answer questions.

    You have access to a fetch_webpage tool, use this to collect
    more information about the topic before responding to the user.
    """,
    description="Simple research agent",
    # tools=[              //exercise-2
    # google_search
    # ]
    tools=[
        fetch_webpage
    ]
)  # Replace this with your Agent definition
