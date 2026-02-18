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
    name="research_agent",
    model="gemini-2.0-flash",
    description="A research assistant that helps users find and understand information.",
    instruction="""You are a helpful research assistant. Your goal is to help users
find information and answer their questions clearly and accurately.

When responding to questions:
1. Provide clear, well-structured answers
2. If you're not sure about something, say so
3. Break down complex topics into understandable parts
4. Cite your reasoning when making claims

Remember: In this version, you don't have access to external tools or
the internet. Answer based on your training knowledge.""",
)
