from bs4 import BeautifulSoup
import requests

def Scrapping(url, html_element, html_class, data_transformer):
  # Extract

  headers = { # use headers to no be detected by web
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
  }

  res = requests.get(url, headers=headers)
  if res.status_code != 200:
    print(f"Error: Blocked or Not Found (Status {res.status_code})")
    return
  
  soup = BeautifulSoup(res.text, "html.parser")

  prices = soup.find_all(html_element, html_class)

  # Transform

  data = []

  for price in prices:
    price_text = price.text
    
    # Transform data for correct append of data
    price_text = data_transformer(price_text)

    price_int = int(float(price_text))
    data.append(price_int)
    
  #print(data) # just to check
  return data
