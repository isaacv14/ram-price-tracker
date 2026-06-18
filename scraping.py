import requests
from bs4 import BeautifulSoup
from crawlbase import CrawlingAPI
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

def Scraping(url, html_element, html_class, data_transformer, html_tag):
  """Scrape prices from a webpage and return as a list of integers."""
  # Extract HTML content
  headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/5.37.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/5.37.36"
  }

  res = requests.get(url, headers=headers)
  if res.status_code != 200:
    print(f"Error: Request failed with status {res.status_code}")
    return [] #empty list if request fails for avoid breaking the rest of the code

  # if there's a custom html tag, use it instead of html class for find the price element
  if html_tag:
    soup = BeautifulSoup(res.text, "html.parser")
    prices = soup.select(html_tag)
  else: # if html class is provided
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

def PlayWrightScraping(url, html_element, html_class, data_transformer):
  """Scrape prices from a webpage and return as a list of integers."""
  headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/5.37.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/5.37.36"
  }
  # Extract HTML content
  with sync_playwright() as p:
    try:
      # Launch a headless browser instance
      browser = p.chromium.launch(headless=True)
      page = browser.new_page()
    except Exception as e:
      print(f"An error occurred while launching the browser: {e}")
      return []
    page.goto(url, wait_until="networkidle")
    
    # Wait for the specific data or dynamic elements to load into the DOM
    page.wait_for_selector(f".{html_class}")
    
    # Extract the fully rendered HTML content
    html_content = page.content()
    browser.close()
  
  soup = BeautifulSoup(html_content, "html.parser")
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

# scrap function using cr awlbase for bypassing anti-scraping


# scrap function using crawlbase for bypassing anti-scraping
load_dotenv()
crawl_api_key = CrawlingAPI({'token': os.getenv('CRAWLBASE_API_KEY')})

def CrawlbaseScrape(url, html_element, html_class, data_transformer):
  data = []

  try:
    response = crawl_api_key.get(url)
    
    if response['status_code'] == 200:
      html_content = response['body']
      #print("Successfully fetched HTML!")
        
      # Check Crawlbase internal router and site status
      #print(f"Original Site Status: {response['headers']['original_status']}")
      #print(f"Crawlbase Route Status: {response['headers']['pc_status']}")
        
      # Next step: Pass 'html_content' to your parser or ETL logic
      soup = BeautifulSoup(html_content, "html.parser")
      prices = soup.find_all(html_element, class_=html_class)

      for price in prices:
        price_text = price.text
        # Apply the site-specific cleaning function
        price_text = data_transformer(price_text)
        price_int = int(float(price_text))
        data.append(price_int)
        
  except Exception as e:
    print(f"An error occurred during extraction: {e}")

  return list(data)