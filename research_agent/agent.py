"""
ADK Workshop - Research Agent

This is your starting point for the workshop exercises.
Follow the instructions in the README to progressively build
your Research Agent from a simple single agent to a full
multi-agent system.

Current Exercise: 1 (Simple Single Agent)
"""

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
    name="Shanks_Research_Agent",
    model="gemini-2.0-flash",
    instruction="You are a helpful research assistant that helps users find information about topics of interest. Your goal " \
    "is to provide accurate and concise information based on user queries. Always strive to be helpful and informative." \
    "" \
    "IMPORTANT INSTRUCTIONS:" \
    "1. You do not have access to any external tools yet.",
    description="An agent that assists with research tasks."
)  # Replace this with your Agent definition
