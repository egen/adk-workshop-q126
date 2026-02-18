"""
ADK Workshop - Research Agent

This is your starting point for the workshop exercises.
Follow the instructions in the README to progressively build
your Research Agent from a simple single agent to a full
multi-agent system.

Current Exercise: 1 (Simple Single Agent)
"""

from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool

from .agents import researcher, fact_checker, critic

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
    name="research_orchestrator",
    model="gemini-2.0-flash",
    description="A research orchestrator that coordinates a team of specialized agents.",
    instruction=(
        "You are a research orchestrator responsible for coordinating a team of "
        "specialized agents to answer complex questions.\n"
        "Your team consists of:\n"
        "1. Researcher Agent: Conducts in-depth research using various tools and resources.\n"
        "2. Fact Checker Agent: Verifies the accuracy and reliability of information "
        "gathered by the Researcher Agent.\n"
        "3. Critic Agent: Evaluates the quality and relevance of the information and "
        "provides feedback to improve the research process.\n"
        "Your task is to delegate tasks to the appropriate agents, synthesize their "
        "findings, and ensure that the final output is accurate, comprehensive, and "
        "well-structured. Use the tools at your disposal to facilitate communication "
        "and collaboration among the agents, and to access external information when "
        "necessary. Always strive for clarity, accuracy, and depth in your research outputs."
    ),
    tools=[
        AgentTool(agent=researcher),
        AgentTool(agent=fact_checker),
        AgentTool(agent=critic),
    ],
    #max_turns=3,   # Limit the number of turns to prevent infinite loops during testing
)
