"""
ADK Workshop - Research Agent

"""

from google.adk.agents import Agent
from google.adk.tools import google_search


root_agent = Agent(
    name = "Simple_Research_Agent",
    model = "gemini-2.0-flash",
    instruction = """You are a helpful research assistant. Your goal is to help users
find information and answer their questions clearly and accurately.

You have access to Google search tool to find and verify information before presenting a response to the user.
""",
description="Simple Research Agent",
tools = [
    google_search
    ]
)  
