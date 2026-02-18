"""
ADK Workshop - Research Agent

This is your starting point for the workshop exercises.
Follow the instructions in the README to progressively build
your Research Agent from a simple single agent to a full
multi-agent system.

Current Exercise: 1 (Simple Single Agent)
"""
from google.adk.agents import Agent

# Exercise: Create a basic knowledge assistant agent

root_agent = Agent(
    name="knowledge_assistant",
    model="gemini-2.0-flash",
    instruction="""
    You are an intelligent and helpful knowledge assistant.
    Your role is to provide clear, concise, and accurate answers
    to user questions based solely on your training knowledge.

    Guidelines:
    - Explain concepts in a simple and structured way.
    - Provide examples when helpful.
    - If you are unsure, respond honestly.
    - Do not assume access to external tools or real-time data.
    """,
    description="A fast and reliable knowledge-based assistant that answers questions clearly without using external tools."
)

 # Replace this with your Agent definition
