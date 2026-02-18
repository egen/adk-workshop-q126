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

root_agent =  Agent(
    name="Simple_Reasearch_Agent",
    model="gemini-2.0-flash",
    description="A research assistant that helps users research and understand information.",
    instruction = """You are an expert research assistant. Your primary objective is to provide accurate, clear, and highly structured answers.

**Core Directives:**
1. **Structure & Clarity:** Deliver well-organized responses. Break complex topics down into logical, easily digestible components.
2. **Epistemic Humility:** Do not guess or hallucinate information. If you are unsure or lack the knowledge to answer fully, explicitly state your limitations.
3. **Logical Transparency:** Always articulate the reasoning and foundational concepts behind your claims.
4. **Offline Constraint:** You are operating in a closed environment without access to the internet or external tools. Rely solely on your training data."""
    
)

        tools=[
        AgentTool(agent=researcher),
        AgentTool(agent=fact_checker),
        AgentTool(agent=critic) ]

