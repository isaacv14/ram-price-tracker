import requests
import os
from dotenv import load_dotenv

# Variables are being exported
url = 'https://listado.mercadolibre.com.mx/memoria-ram'
html_element = "span"
html_class = "andes-money-amount__fraction"

# Loading Key en .env
load_dotenv()
api_key = os.getenv('CURRENCY_MX_API_KEY')

currency_API = requests.get(f'https://api.currencyapi.com/v3/latest?apikey={api_key}&currencies=MXN')
currency_value = currency_API.json().get('data').get('MXN').get('value')

# Function called in main to be used in Scrapping function
def cleaning_function(price_text):
  data_cleaned = price_text.replace(",","")

  usd_parse = int(data_cleaned) / currency_value
  return str(usd_parse)
