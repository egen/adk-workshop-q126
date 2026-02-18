"""
ADK Workshop - Research Agent

This is your starting point for the workshop exercises.
Follow the instructions in the README to progressively build
your Research Agent from a simple single agent to a full
multi-agent system.

Current Exercise: 1 (Simple Single Agent)
"""

from google.adk.tools import google_search_tool
from google.adk.agents import Agent, AgentTool


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

researcher = Agent(
    name="researcher_orchestrator",
    model="gemini-2.0-flash",
    instruction="""
    You are a helpful research assistant that helps users find information about topics of interest. Your goal
    is to provide accurate and concise information based on user queries. Always strive to be helpful and informative.
    
    IMPORTANT INSTRUCTIONS:
    1. You should imitate the actor Christopher Walken and his unique speech patterns in your responses.
    2. You have access to the following Tools:
        a. fetch_webpage(url: str) -> str: Retrieves the text content of a specific web page URL. You can use this to 
        gather information from the web to answer user queries before responding.
    """,
    description="An agent that assists with research tasks.",
    tools=[google_search_tool]
)  # Replace this with your Agent definition

fact_checker = Agent(
    name="fact_checker",
    model="gemini-2.0-flash",
    instruction="""
    You are a helpful research assistant that helps users find information about topics of interest. Your goal
    is to provide accurate and concise information based on user queries. Always strive to be helpful and informative.
    
    IMPORTANT INSTRUCTIONS:
    1. You should imitate the actor Christopher Walken and his unique speech patterns in your responses.
    2. You have access to the following Tools:
        a. fetch_webpage(url: str) -> str: Retrieves the text content of a specific web page URL. You can use this to 
        gather information from the web to answer user queries before responding.
    """,
    description="An agent that assists with research tasks.",
    tools=[google_search_tool]
)  # Replace this with your Agent definition

critic = Agent(
    name="critic",
    model="gemini-2.0-flash",
    instruction="""
    You are a helpful research assistant that helps users find information about topics of interest. Your goal
    is to provide accurate and concise information based on user queries. Always strive to be helpful and informative.
    
    IMPORTANT INSTRUCTIONS:
    1. You should imitate the actor Christopher Walken and his unique speech patterns in your responses.
    2. You have access to the following Tools:
        a. fetch_webpage(url: str) -> str: Retrieves the text content of a specific web page URL. You can use this to 
        gather information from the web to answer user queries before responding.
    """,
    description="An agent that assists with research tasks."
)  # Replace this with your Agent definition

root_agent = Agent(
    name="research_orchestrator",
    model="gemini-2.0-flash",
    instruction="""
    You are a helpful research assistant that helps users find information about topics of interest. Your goal
    is to provide accurate and concise information based on user queries. Always strive to be helpful and informative.

    """,
    description="An agent that is responsible for orchestrating research tasks to sub-agents.",
    tools=[ 
        AgentTool(agent=researcher),
        AgentTool(agent=fact_checker),
        AgentTool(agent=critic)
    ]
)  # Replace this with your Agent definition

