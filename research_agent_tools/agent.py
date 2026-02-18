"""
ADK Workshop - Research Agent

This is your starting point for the workshop exercises.
Follow the instructions in the README to progressively build
your Research Agent from a simple single agent to a full
multi-agent system.

Current Exercise: 2 (Simple Single Agent with Tools)
"""

from google.adk.agents import Agent
from google.adk.tools import google_search

# create a Google ADK agent
root_agent = Agent(
    name="Research_Agent_tools_impl",
    model="gemini-2.0-flash",
    description="A simple research agent that can answer questions and provide information with some tools.",
    instruction="""
    You are a helpful research assistant. Answer questions and provide information based on your knowledge
    and the tools available to you.

    When answering questions:
    1. Provide clear and concise answers.
    2. If any information is not clear, ask clarifying questions before providing an answer.
    3. Use the tools at your disposal to find information when needed.
    4. Always cite your sources when providing information.
    5. You have access to the listed tools, use them effectively to verify information and assist 
    users in finding and understanding information.

     Remember, you are here to assist users in finding and understanding information effectively.
    """,
    tools=[
        google_search
    ],
        
)
