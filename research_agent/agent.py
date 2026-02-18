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
    model="gemini-2.0-flash",
    instruction="""
        You are a helpful research assistant that answers questions about the provided topics.
        When given a question, use the provided information to generate a concise and accurate answer.
        Remember: You do not have access to external information beyond what is provided in the input. 
        Focus on using the given data to formulate your response.""",
    description="A simple agent that helps with basic research tasks.",
)
