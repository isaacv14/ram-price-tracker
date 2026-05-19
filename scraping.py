from bs4 import BeautifulSoup
import requests

def Scraping(url, html_element, html_class, data_transformer):
  """Scrape prices from a webpage and return as a list of integers."""
  # Extract HTML content
  headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/5.37.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/5.37.36"
  }

  res = requests.get(url, headers=headers)
  if res.status_code != 200:
    print(f"Error: Request failed with status {res.status_code}")
    return [] #empty list if request fails for avoid breaking the rest of the code

  soup = BeautifulSoup(res.text, "html.parser")
  prices = soup.find_all(html_element, class_=html_class)

  # Transform raw HTML text into clean numeric data
  data = []

  for price in prices:
    price_text = price.text
    # Apply the site-specific cleaning function
    price_text = data_transformer(price_text)
    price_int = int(float(price_text))
    data.append(price_int)

  return list(data)
