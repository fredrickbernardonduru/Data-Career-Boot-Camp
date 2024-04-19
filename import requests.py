import requests
from bs4 import BeautifulSoup

# Define the URL of the website to scrape
url = 'https://www.example.com'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the <a> tags containing links
    links = soup.find_all('a')
    
    # Extract and print the text and href attribute of each link
    for link in links:
        link_text = link.text.strip()
        href = link.get('href')
        print(f"Link Text: {link_text}, Href: {href}")
else:
    print('Failed to retrieve the webpage')
