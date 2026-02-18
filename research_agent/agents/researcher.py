"""
Researcher Agent - Performs broad web research on a given topic.
"""

from google.adk.agents import Agent
from google.adk.tools import google_search

researcher = Agent(
    name="researcher",
    model="gemini-2.0-flash",
    description="Performs broad web research on a topic using Google Search. Give this agent a research query.",
    instruction="""You are a research specialist. Given a topic or question, use google_search
to find comprehensive information.

Search Strategy:
1. Run 2-3 targeted searches with different phrasings to get broad coverage
2. Focus on authoritative sources: official sites, academic papers, reputable news
3. Look for specific facts, statistics, and expert opinions

Output Format:
Return a structured summary of your findings, organized by subtopic.
Include specific facts, figures, and details wherever possible.""",
    tools=[google_search],
)
