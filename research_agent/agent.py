"""
ADK Workshop - Research Agent

This is your starting point for the workshop exercises.
Follow the instructions in the README to progressively build
your Research Agent from a simple single agent to a full
multi-agent system.

Current Exercise: 2 (Agent with Tools)
"""

from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="simple_research_agent",
    model="gemini-2.0-flash",
    instruction="""
You are a helpful research assistant. Your goal is to help users
find information and answer questions.

You have access to a Google search tool to find and verify information
before presenting a response to the user.
""",
    description="Simple research agent",
    tools=[
        google_search
    ]
)
