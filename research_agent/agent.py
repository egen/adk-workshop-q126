"""
ADK Workshop - Research Agent

This is your starting point for the workshop exercises.
Follow the instructions in the README to progressively build
your Research Agent from a simple single agent to a full
multi-agent system.

Current Exercise: 1 (Simple Single Agent)
"""

from google.adk.agents import Agent
from google.adk.tools import google_search

# Exercise 1: Create a simple researc
root_agent = Agent(
    name="simple_research_agent",
    model="gemini-2.0-flash",
    instruction="""
    You are a helpful research assistant. Your goal is to help users find accurate and relevant information.
    Remember to provide clear and concise answers, and if you don't know something, it's okay to say so.
    you have access to google search tool to find and verify information before presneting it to the user.
    """
    description="A simple research agent for the ADK Workshop."
    tools=[google_search]
)