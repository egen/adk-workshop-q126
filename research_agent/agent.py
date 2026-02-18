"""
ADK Workshop - Research Agent

This is your starting point for the workshop exercises.
Follow the instructions in the README to progressively build
your Research Agent from a simple single agent to a full
multi-agent system.

Current Exercise: 1 (Simple Single Agent)
"""

import requests
from bs4 import BeautifulSoup
from google.adk.agents import Agent
from google.adk.tools import google_search_tool

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

def fetch_webpage(url: str) -> str:
    """
    Retrieves the text content of a specific web page URL.
    
    Args:
        url: The full URL, including the protocol (https), to fetch (e.g., "https://www.example.com") the HTML contents
        of the webpage. 
        
    Returns:
        The text content of the page, or an error message.
    """
    try:
        # 1. Get the page
        headers = {'User-Agent': 'Mozilla/5.0'} # Mimic a browser to avoid 403 errors
        response = requests.get(url, headers=headers, timeout=10)
        
        # 2. Check for success
        if response.status_code != 200:
            return f"Error: Failed to load page. Status code: {response.status_code}"
            
        # 3. Parse the HTML to get just the text
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements to clean up the output
        for script in soup(["script", "style"]):
            script.extract()
            
        text = soup.get_text()
        
        # Collapse whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        clean_text = '\n'.join(chunk for chunk in chunks if chunk)
        
        # Limit length to avoid overflowing the context window
        return clean_text[:5000] 

    except Exception as e:
        return f"Error fetching page: {str(e)}"

root_agent = Agent(
    name="Shanks_Research_Agent",
    model="gemini-2.0-flash",
    instruction="""
    You are a helpful research assistant that helps users find information about topics of interest. Your goal
    is to provide accurate and concise information based on user queries. Always strive to be helpful and informative.
    
    IMPORTANT INSTRUCTIONS:
    1. You should imitate the actor Christopher Walken and his unique speech patterns in your responses.
    2. You have access to the following Tools:
        a. fetch_webpage(url: str) -> str: Retrieves the text content of a specific web page URL.
        b. google_search_tool(query: str) -> List[str]: Performs a Google search to find and verify information.
    """,
    description="An agent that assists with research tasks.",
    tools=[fetch_webpage, google_search_tool ]
)  # Replace this with your Agent definition