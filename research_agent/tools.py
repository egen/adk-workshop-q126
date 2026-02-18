"""
Exercise 2: Custom Tools for the Research Agent

This module contains a custom tool that extends the agent's capabilities
for fetching and reading web pages.
"""

import requests
from bs4 import BeautifulSoup


def fetch_webpage(url: str) -> dict:
    """
    Fetches the content of a webpage and extracts the main text.

    Use this tool when you need to read the content of a specific webpage
    that the user has provided or that you found through search.

    Args:
        url: The full URL of the webpage to fetch (must include http:// or https://)

    Returns:
        A dictionary with status and either the page content or an error message
    """
    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return {
                "status": "error",
                "error_message": f"Failed to fetch URL. HTTP status: {response.status_code}"
            }

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove script and style elements
        for element in soup(["script", "style", "nav", "footer", "header"]):
            element.decompose()

        # Get text content
        text = soup.get_text(separator="\n", strip=True)

        # Truncate if too long
        if len(text) > 10000:
            text = text[:10000] + "\n\n[Content truncated...]"

        return {
            "status": "success",
            "content": text,
            "title": soup.title.string if soup.title else "No title"
        }

    except requests.RequestException as e:
        return {
            "status": "error",
            "error_message": f"Network error: {str(e)}"
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error fetching webpage: {str(e)}"
        }
