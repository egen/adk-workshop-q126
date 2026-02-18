"""
ADK Workshop - Research Agent

This is your starting point for the workshop exercises.
Follow the instructions in the README to progressively build
your Research Agent from a simple single agent to a full
multi-agent system.

Current Exercise: 1 (Simple Single Agent)
"""

from google.adk.agents import Agent
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

root_agent = Agent(
    name="simple_research_agent",
    model="gemini-2.0-flash",
    instruction="""
        You are a Research Agent designed to perform research tasks and summarize findings.
        Your primary function is to gather information on a given topic, analyze it, and provide concise summaries.

        You have access to fetch_webpage tool to find relevant information on the web. Use it to gather data and insights on the topic you are researching.
    """,
    description="Simple Research Agent",
    tools=["fetch_webpage"]  
)  # Replace this with your Agent definition
