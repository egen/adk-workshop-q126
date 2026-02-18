"""
ADK Workshop - Research Agent

This is your starting point for the workshop exercises.
Follow the instructions in the README to progressively build
your Research Agent from a simple single agent to a full
multi-agent system.

Current Exercise: 1 (Simple Single Agent)
"""

from google.adk.agents import Agent
from google.adk.tools import google_search_tool

root_agent = Agent(
    name="Simple Research Agent",
    model="gemini-2.0-flash",
    instruction="""
    You are a helpful research assistant. Your goal is to help users
    find information and answer questions.

    You have access to a google search tool to find and verify information before presenting a response to the user.
    """,
    description="Simple research agent"
    tools=[
        google_search_tool
    ]
)
