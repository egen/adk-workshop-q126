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


root_agent = Agent(
    name="simple_research_agent",
    model="gemini-2.0-flash",
    instruction="""
    You are a helpful research assistant. Your goal is to help users
    find information and answer questions.

    You have access to a fetch_webpage tool, use this to collect
    more information about the topic before responding to the user.
    """,
    description="Simple research agent",
    tools=[
        fetch_webpage
    ]
)
