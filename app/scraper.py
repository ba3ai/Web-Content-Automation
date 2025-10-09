import requests
from bs4 import BeautifulSoup
import os

# Load API credentials from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")
def scrape_google_results(keyword,num_results=10):
    """
    Scrape Google search results using the Custom Search API.

    Args:
        keyword (str): The search query.
        api_key (str): Your Google Custom Search API key.
        cx (str): Your Custom Search Engine ID.
        num_results (int): Number of results to return (max 10 per request).

    Returns:
        list of tuples: (title, link) for each result.
    """
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": keyword,
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_CSE_ID,
        "num": num_results,
    }
    res = requests.get(url, params=params)
    res.raise_for_status()
    data = res.json()

    results = []
    for item in data.get("items", []):
        title = item.get("title", "No title")
        link = item.get("link", "")
        results.append((title, link))
    return results
