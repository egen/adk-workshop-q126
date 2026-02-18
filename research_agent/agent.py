"""
ADK Workshop - Research Agent

This is your starting point for the workshop exercises.
Follow the instructions in the README to progressively build
your Research Agent from a simple single agent to a full
multi-agent system.

Current Exercise: 1 (Simple Single Agent)
"""

from google.adk.agents import Agent

root_agent = Agent(
    name = "Extensive_Research_Agent",
    model = "gemini-2.0-flash",
    instruction = """
    You're a extensive research agent. Your task is to help users find answers to their questions.
    
    Remember not to use any external tools or APIs. Provide accurate information based on your training data and reasoning. Make sure to ask follow up questions and minimize assumptions. If you don't know the answer, say you don't know. 
    """,
    description = "An agent that can answer questions based on its training data and reasoning."
)
