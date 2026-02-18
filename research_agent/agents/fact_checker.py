"""
Fact Checker Agent - Independently verifies claims from the research.

Invoked as an AgentTool by the orchestrator. Uses Google Search to
run independent verification searches on key claims, confirming or
contradicting the initial research findings.
"""

from google.adk.agents import Agent
from google.adk.tools import google_search

fact_checker = Agent(
    name="fact_checker",
    model="gemini-2.0-flash",
    description="Independently verifies claims using Google Search. Give this agent the claims to verify.",
    instruction="""You are a fact checker. Your job is to independently verify claims
from research findings by running your own searches.

Verification Process:
1. Identify the key factual claims in the content you receive
2. Use google_search to independently verify each major claim
3. Look for supporting or contradicting evidence

Output Format:
For each claim you check, report:
- The claim
- VERIFIED, PARTIALLY VERIFIED, or UNVERIFIED
- Supporting or contradicting evidence found

Be thorough but focus on the most important and specific claims
(numbers, dates, statistics, named facts). Skip subjective opinions.""",
    tools=[google_search],
)
