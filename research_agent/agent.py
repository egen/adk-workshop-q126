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

root_agent = Agent(
    name="research_agent_with_search",
    model="gemini-2.0-flash",
    instruction="""
    You are a research assistant with access to Google Search.

    Guidelines:
    - Always use the google_search tool for current events or factual queries.
    - Summarize the information clearly.
    - Cite sources when possible.
    - Do not make up information.
    """,
    description="A research assistant that uses Google Search to provide accurate and up-to-date answers.",
    tools=[google_search]   
)


 # Replace this with your Agent definition
