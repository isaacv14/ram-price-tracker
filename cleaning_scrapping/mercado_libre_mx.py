# Variables are being exported

url = 'https://listado.mercadolibre.com.mx/memoria-ram'
html_element = "span"
html_class = "andes-money-amount__fraction"

def cleaning_function(price_text):
  return price_text.replace(",","")

