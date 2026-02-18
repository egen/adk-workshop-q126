"""
Exercise 1 Solution: Simple Single Agent

This is a basic research agent that can answer questions using its
built-in knowledge. It doesn't have any tools yet - that comes in Exercise 2.
"""

from google.adk.agents import Agent

root_agent = root_agent = Agent(
	name="research_agent-1",
	model="gemini-4.0-flash",
	description="A research assistant that helps users find and understand information.",
	instruction="You are a helpful research assistant. Provide clear, well-structured answers based on your training knowledge. If uncertain, say so.",
)
