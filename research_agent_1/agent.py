from google.adk.agents import Agent

root_agent = Agent(
    name="research_agent_1",
    model="gemini-2.0-flash",
    description="First research assistant variant.",
    instruction="You are a helpful research assistant. Provide clear, well-structured answers based on your training knowledge. If uncertain, say so.",
)
