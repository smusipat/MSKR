import requests
from bs4 import BeautifulSoup

def search_google_jobs(role, location=None):
    url = "https://www.google.com/search"
    params = {
        "q": f"jobs {role}",
        "tbm": "nws"
    }
    if location:
        params["q"] += f" {location}"
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, "html.parser")
    job_links = [a["href"] for a in soup.find_all("a", href=True) if "https://www.google.com/url?q=" in a["href"]]
    return job_links

role = "Product Manager"
location = "New York"
job_links = search_google_jobs(role, location)
for link in job_links:
    print(link)