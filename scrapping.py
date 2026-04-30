from bs4 import BeautifulSoup
import requests
import pandas as pd

# Extract

url = 'https://listado.mercadolibre.com.mx/memoria-ram'
headers = { # use headers to no be detected by web
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

prices = soup.find_all("span", class_="andes-money-amount__fraction")

# Transform

data = []

for price in prices:
  price_text = price.text
  find_coma = price_text.find(",")

  if find_coma != -1: # if comma was found, remove it
    price_text = price_text.replace(",","")

  price_int = int(price_text)
  data.append(price_int)

