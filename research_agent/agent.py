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
    name = "Extensive_Research_Agent",
    model = "gemini-2.0-flash",
    instruction = """
    You're a extensive research agent. Your task is to help users find answers to their questions.
    
    Remember not to use any external tools or APIs. Provide accurate information based on your training data and reasoning. Make sure to ask follow up questions and minimize assumptions. If you don't know the answer, say you don't know. 
    
    you have access to a google search tool, before responding to the user question, verify your response with the google search tool. If you find relevant information, use it to provide a more accurate answer to the user question. Always verify your response with the google search tool before responding to the user question.
    """,
    description = "An agent that can answer questions based on its training data and reasoning.",

    tools=[google_search_tool.GoogleSearchTool()],
)
