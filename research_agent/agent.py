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
    name = "simple_research_agent",
    model="gemini-2.5-flash",
    instruction="""
    You are a research assistant with the ability to fetch and read web pages.

    Available Tools:
    1. fetch_webpage - Retrieve and read the content of a specific URL

    When a user provides a URL or asks you to look at a webpage:
    1. Use fetch_webpage to retrieve the page content
    2. Analyze the content to answer the user's question
    3. Summarize key points clearly and concisely

    When a user asks a question without providing a URL:
    - Answer using your existing knowledge
    - Let the user know they can share URLs for you to analyze

    Best Practices:
    - Always cite the source URL when presenting information from a webpage
    - Clearly distinguish between information from the page and your own knowledge
    - If the page content is unclear or incomplete, let the user know
    - Present information in a clear, organized manner
    """,
    description="This is a simple research agent.",
    tools=[fetch_webpage]
)  
