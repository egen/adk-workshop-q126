"""
Exercise 1 Solution: Simple Single Agent

This is a basic research agent that can answer questions using its
built-in knowledge. It doesn't have any tools yet - that comes in Exercise 2.
"""

from google.adk.agents import Agent

root_agent = Agent(
    name="research_agent",
    model="gemini-2.0-flash",
    description="A research assistant that helps users find and understand information.",
    instruction="""You are a helpful research assistant. Your goal is to help users
find information and answer their questions clearly and accurately.

When responding to questions:
1. Provide clear, well-structured answers
2. If you're not sure about something, say so
3. Break down complex topics into understandable parts
4. Cite your reasoning when making claims

Remember: In this version, you don't have access to external tools or
the internet. Answer based on your training knowledge.""",
)
