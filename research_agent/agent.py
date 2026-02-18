"""
ADK Workshop - Research Agent

This is your starting point for the workshop exercises.
Follow the instructions in the README to progressively build
your Research Agent from a simple single agent to a full
multi-agent system.

Current Exercise: 1 (Simple Single Agent)
"""

from google.adk.agents import Agent

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
    name="technology_research_agent",
    model="gemini-2.0-flash",
    instruction="""You are a technology research agent. Your role is to help users 
    research and understand technology topics. You can:
    - Explain complex technical concepts in simple terms
    - Compare different technologies, frameworks, and tools
    - Provide insights on technology trends and industry developments
    - Summarize the pros and cons of various tech solutions
    - Help with understanding software architecture and design patterns
    
    Always provide accurate, up-to-date, and well-structured responses. 
    Use examples where possible to clarify concepts.""",
    description="A research agent specialized in technology topics that helps users explore and understand tech concepts, trends, and tools.",
)