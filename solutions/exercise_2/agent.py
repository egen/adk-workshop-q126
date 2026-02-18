"""
Exercise 2 Solution: Single Agent with Tools

This research agent has a custom tool for fetching and reading web pages,
demonstrating how to extend an agent's capabilities with function tools.
"""

from google.adk.agents import Agent

from google.adk.tools import google_search

root_agent = Agent(
    name="research_agent-2",
    model="gemini-2.0-flash",
    description="A research assistant that can fetch and read web pages to help answer questions.",
    instruction="""You are a research assistant with the ability to fetch and read web pages.

    You have access to Google Search to find relevant information.
    """,
    tools=[google_search],
)
