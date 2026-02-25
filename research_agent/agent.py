from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name= "simple_research_agent",
    model="gemini-2.0-flash",
    instruction="""
    You are a helpful research assistance. Your goal is to help users 
    find information and answer questions. 
    
    You have access to Google search tool to find and verify information 
    before presenting a response to the user.
    """,
    description="Simple research agent",
    tools = [
        google_search
    ]
)  