"""
Exercise 4: Flawed Agent for Evaluation Demo

This orchestrator has intentional issues in its instruction prompt:
1. Skips fact_checker — doesn't verify any claims
2. Skips critic — doesn't identify weaknesses or gaps
3. Vague instructions with no enforced workflow

Use this agent to demonstrate how evaluation catches these issues.
"""

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .agents import researcher, fact_checker, critic

root_agent = Agent(
    name="research_orchestrator",
    model="gemini-2.0-flash",
    description="An orchestrator agent that coordinates sub-agents to perform research.",
    instruction="""You are a research assistant. You have some helper agents available.

Your helpers:
- researcher: Can search the web for information
- fact_checker: Can verify claims
- critic: Can review findings

When a user asks you to research something, use researcher to find information
and then write up a report based on what you find. Try to be helpful and
give good answers. Make the report look nice with markdown formatting.""",
    tools=[
        AgentTool(agent=researcher),
        AgentTool(agent=fact_checker),
        AgentTool(agent=critic),
    ],
)
