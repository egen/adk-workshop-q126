"""
ADK Workshop - Research Agent

This is your starting point for the workshop exercises.
Follow the instructions in the README to progressively build
your Research Agent from a simple single agent to a full
multi-agent system.

Current Exercise: 1 (Simple Single Agent)
"""

from google.adk.agents import Agent
from .tools import fetch_web_content

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
    name="Research_Agent",
    model="gemini-2.5-flash",
    instruction="""\
    You are a research assistant. 
    Help with gathering and analyzing information.

    You have access to the following tools:
        - fetch_web_content(url): Use this tool to collection more information about the topic before responding.
            Fetches the textual content of a web page and extracts the main text.
    """,
    description="A simple research agent for the ADK Workshop.",
    tools=[fetch_web_content]  # Add the web content fetching tool
)

# root_agent = None  # Replace this with your Agent definition
