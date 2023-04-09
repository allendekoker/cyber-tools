import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Parse the HTML content of the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the links on the page
    links = soup.find_all('a')

    # Extract the text and href attribute of each link
    for link in links:
        text = link.get_text()
        href = link.get('href')
        print(f'{text}: {href}')
