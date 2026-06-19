import requests
from bs4 import BeautifulSoup

def Scraping_test(url, html_element, html_class, data_transformer, html_tag):
  """Scrape prices from a webpage and return as a list of integers."""
  # Extract HTML content
  headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/5.37.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/5.37.36"
  }

  res = requests.get(url, headers=headers)
  if res.status_code != 200:
    print(f"Error: Request failed with status {res.status_code}")
    return [] #empty list if request fails for avoid breaking the rest of the code

  print("----------------------------------------------------------")
  print(res.text) # Print the raw HTML content for debugging
  print("----------------------------------------------------------")

  # if there's a custom html tag, use it instead of html class for find the price element
  if html_tag:
    soup = BeautifulSoup(res.text, "html.parser")
    prices = soup.select(html_tag)
  else: # if html class is provided
    soup = BeautifulSoup(res.text, "html.parser")
    prices = soup.find_all(html_element, class_=html_class)

  # Transform raw HTML text into clean numeric data
  print(prices)
  print("----------------------------------------------------------")