import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1').text if soup.find('h1') else 'No title found'
        content = ' '.join(p.text for p in soup.find_all('p'))
        return title, content
    else:
        return None, None

url = 'https://www.economist.com/the-world-in-brief'
title, content = scrape_article(url)
if title and content:
    print(f"Title: {title}")
    print(f"Content: {content[:500]}...")  # Print the first 500 characters of the content
else:
    print("Failed to retrieve the article")
