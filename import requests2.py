import requests
from bs4 import BeautifulSoup

def scrape_product_data(url):
  """
  This function scrapes product information from a given URL.
  """
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    soup = BeautifulSoup(response.content, "html.parser")

    # Extract product title, price, and description using selectors (replace with specific website selectors)
    title_element = soup.find("h1", class_="product-title")
    price_element = soup.find("span", class_="product-price")
    description_element = soup.find("div", class_="product-description")

    if title_element and price_element and description_element:
      product_data = {
          "title": title_element.text.strip(),
          "price": price_element.text.strip(),
          "description": description_element.text.strip()
      }
      return product_data
    else:
      print(f"Failed to extract data from {url}")
      return None

  except requests.exceptions.RequestException as e:
    print(f"Error occurred while fetching data: {e}")
    return None

# Example usage
url = "https://www.example.com/products/123"
product_info = scrape_product_data(url)

if product_info:
  print(f"Product Title: {product_info['title']}")
  print(f"Price: {product_info['price']}")
  print(f"Description: {product_info['description']}")
else:
  print("Data scraping failed.")
