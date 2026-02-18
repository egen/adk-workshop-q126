"""
Exercise 4: Fixed Agent Solution

This is the corrected orchestrator with proper workflow instructions.
Compare this to flawed_agent.py to see the improvements.

Key fixes:
1. Explicit workflow steps (RESEARCH → VERIFY → CRITIQUE → REPORT)
2. Mandatory use of all three agents in sequence
3. Quality standards requiring verified claims and addressed criticism
4. Clear delegation guidelines for each agent
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

IMPORTANT: You MUST use all three agents in sequence. Never skip the fact_checker
or critic steps — unverified and unchallenged research is unreliable.

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
