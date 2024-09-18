import requests
from bs4 import BeautifulSoup

def build_search_url(role: str, location: str = None) -> str:
    """Build the Google search URL"""
    url = "https://www.google.com/search"
    params = {
        "q": f"jobs {role}",
        "tbm": "nws"
    }
    if location:
        params["q"] += f" {location}"
    return url + "?" + "&".join(f"{k}={v}" for k, v in params.items())

def fetch_search_results(url: str) -> str:
    """Fetch the search results HTML"""
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    return response.text

def extract_job_links(html: str) -> list:
    """Extract job links from the search results HTML"""
    soup = BeautifulSoup(html, "html.parser")
    job_links = []
    for a in soup.find_all("a", href=True):
        if "https://www.google.com/url?q=" in a["href"]:
            job_links.append(a["href"])
    return job_links

def search_google_jobs(role: str, location: str = None) -> list:
    """Search for jobs on Google"""
    url = build_search_url(role, location)
    html = fetch_search_results(url)
    return extract_job_links(html)

role = "Product Manager"
location = "New york"
job_links = search_google_jobs(role, location)
for link in job_links:
    print(link)