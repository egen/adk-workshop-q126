import requests
from bs4 import BeautifulSoup
from typing import Dict


def fetch_web_content(url: str) -> Dict[str, str]:
    """
    Fetches the textual content of a web page and extracts the main text.
    
    Args:
        url: The URL of the web page to fetch.
    
    Returns:
        The extracted text content of the web page, in json format
    """
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            # Log the error and return json if the request was not successful
            print(f"Failed to fetch {url}: Status code {response.status_code}")
            return {"error": f"Failed to fetch {url}: Status code {response.status_code}"}
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')

        #  extract the main text content from the page and return in json format
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