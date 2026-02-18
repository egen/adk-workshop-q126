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
    name="simple_research_agent",
   model="gemini-3-pro-preview",
    instruction="""
    You are a helpful research assistant. Your goal is to help users
    find information and answer questions.

    Remember: In this version you do not have access to any tools and
    all information must come from your training knowledge.
    """,
    description="Simple research agent"
)
