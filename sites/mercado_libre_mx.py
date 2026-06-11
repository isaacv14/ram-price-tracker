import requests
import os
from dotenv import load_dotenv

# Mercado Libre Mexico RAM listing configuration
url = 'https://listado.mercadolibre.com.mx/memoria-ram'
html_element = "span"
html_class = "andes-money-amount__fraction"

# Load API key from .env file
load_dotenv()
api_key = os.getenv('CURRENCY_MX_API_KEY')

# Fetch current USD to MXN exchange rate
currency_API = requests.get(f'https://api.currencyapi.com/v3/latest?apikey={api_key}&currencies=MXN')
currency_value = currency_API.json().get('data').get('MXN').get('value')

def cleaning_function(price_text):
  """Clean price text and convert from MXN to USD."""
  # Remove thousand separators
  data_cleaned = price_text.replace(",","")

  # Convert to USD using the current exchange rate
  if currency_value:
    usd_parse = int(data_cleaned) / currency_value
    return str(usd_parse)

  usd_parse = int(data_cleaned) / 17.5
  print("Error fetching exchange rate. Using default conversion rate of 17.5 MXN to 1 USD.")
  return str(usd_parse)