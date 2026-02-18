"""
Exercise 3 Solution: Multi-Agent Research Pipeline

An orchestrator agent that invokes specialized sub-agents as tools
to perform end-to-end research from a single user prompt. Only the
orchestrator's final output is visible to the user.

Architecture:
    research_orchestrator (Agent)
    ├── researcher     (AgentTool) - Broad web research via Google Search
    ├── fact_checker   (AgentTool) - Independent verification via Google Search
    └── critic         (AgentTool) - Challenges findings and identifies gaps
"""

from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

from .agents import researcher, fact_checker, critic

root_agent = Agent(
    name="research_orchestrator",
    model="gemini-2.0-flash",
    description="A research orchestrator that coordinates a team of specialized agents.",
    instruction="""You lead a research team. For every research request, follow this
exact workflow:

1. RESEARCH: Use researcher to gather broad information on the topic
2. VERIFY: Use fact_checker to independently verify the key claims
3. CRITIQUE: Use critic to challenge the findings and identify weaknesses or gaps
4. REPORT: Write the final polished report yourself, incorporating verified facts
   and addressing the critic's feedback

Your final report must include:
- A clear title
- An executive summary (2-3 sentences)
- Detailed findings organized by theme, noting which claims were verified
- A section addressing limitations or open questions raised by the critic

Writing Guidelines:
- Use clear, professional language
- Use markdown formatting for readability
- Lead with the most important information
- Be transparent about what was verified vs. what could not be confirmed""",
    tools=[
        AgentTool(agent=researcher),
        AgentTool(agent=fact_checker),
        AgentTool(agent=critic),
    ],
)
