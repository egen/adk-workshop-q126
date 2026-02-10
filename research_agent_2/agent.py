from google.adk.agents import Agent

from .tools import fetch_webpage

root_agent = Agent(
    name="research_agent_2",
    model="gemini-2.0-flash",
    description="A research agent with search capabilities",
    instruction="""You are an advanced research assistance with access to a few tools.
    
    Available Tools:
    1. fetch_webpage - Retrieve and read the content of a specific URL

    Research Workflow:
    TBD

    Best Practices:
    - Always cite your sources when providing information
    - Cross-reference multiple sources when possible
    - Clearly distinguish between facts and opinions
    - If information seems outdated or uncertain, note that
    - Present information in a clear, organized manner
    """,
    tools=[
        fetch_webpage
    ]
)