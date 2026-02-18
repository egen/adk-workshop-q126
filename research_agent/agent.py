"""
ADK Workshop - Research Agent

This is your starting point for the workshop exercises.
Follow the instructions in the README to progressively build
your Research Agent from a simple single agent to a full
multi-agent system.

Current Exercise: 1 (Simple Single Agent)
"""

from google.adk.agents import Agent
from tools import fetch_webpage

root_agent = Agent(
    name="Research_Agent_basic",
    model="gemini-2.0-flash",
    instruction="""You are a helpful research assistant. 
    
    Remeber: Answer questions based on your knowledge and reasoning.

    If you don't know the answer, say so.
    You have access to the fetch_webpage tool, which you can use to find information on the web.
    Make use of it to answer the user's questions.
    """,
    
    description="A simple research agent",
    tools=[fetch_webpage]
)
