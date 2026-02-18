"""
ADK Workshop - Research Agent

This is your starting point for the workshop exercises.
Follow the instructions in the README to progressively build
your Research Agent from a simple single agent to a full
multi-agent system.

Current Exercise: 1 (Simple Single Agent)
"""

from requests import __description__
from google.adk.agents import Agent

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
    name="Simple Research Agent",
    model="gemini-2.0-flash",
    instruction="""Help me write my research agent with following points to consideR:
1. you are helpful research agent
2. Your goal is to find accurate information and answer for questions
3. Remmeber: all tools if you ghave but you dont"""
)

root_agent = root_agent  # Replace this with your Agent definition
