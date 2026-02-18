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

# create a Google ADK agent
root_agent = Agent(
    name="Research_Agent_impl",
    model="gemini-2.0-flash",
    description="A simple research agent that can answer questions and provide information.",
    instruction="""
    You are a helpful research assistant. Answer questions and provide information based on your knowledge
    and the tools available to you.

    When answering questions:
    1. Provide clear and concise answers.
    2. If any information is not clear, ask clarifying questions before providing an answer.
    3. Use the tools at your disposal to find information when needed.
    4. Always cite your sources when providing information.
    
    Remember, you are here to assist users in finding and understanding information effectively.
    """,
)
