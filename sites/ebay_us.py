url = "https://www.ebay.com/b/Computer-Memory-RAM/170083"
html_element = "span"
html_class = "bsig__price--displayprice"

def cleaning_function(price_text):
  """Clean price text and convert from MXN to USD."""
  # Remove thousand separators
  data_cleaned = price_text.replace("$","").replace(",","").replace("USD1\xa0","").replace("USD","").strip()

  return str(data_cleaned)
