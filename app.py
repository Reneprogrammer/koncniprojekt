import streamlit as st
import requests
from bs4 import BeautifulSoup

def scrape_article(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        article_divs = soup.find_all('div', class_='css-1qiat4j')
        content = ' '.join(div.text for div in article_divs)
        return content
    else:
        return None

st.title("Article Scraper")
url = st.text_input("Enter the article URL:")
if url:
    content = scrape_article(url)
    if content:
        st.write(content)
    else:
        st.write("Failed to retrieve the article")
