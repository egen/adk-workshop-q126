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
root_agent = Agent(
    name="research_helper",
    model="gemini-2.0-flash",
    instructions="""
    You are an intelligent and reliable research assistant.
    Your responsibility is to provide clear, concise, and accurate
    answers based only on your existing training knowledge.

    IMPORTANT:
    - You do not have access to external tools, APIs, or live internet data.
    - Do not claim to search the web or access real-time information.
    - Base all responses strictly on your internal knowledge.
    - If you are unsure about something, state your uncertainty honestly.
    """,
    description="An AI research assistant that provides knowledge-based answers without external tools."
)

root_agent = None

 # Replace this with your Agent definition
