url = "https://www.ebay.com/b/Computer-Memory-RAM/170083"
html_element = "span"
html_class = "bsig__price--displayprice"

def cleaning_function(price_text):
  """Clean price text specific to eBay US"""
  # Remove thousand separators
  data_cleaned = price_text.replace("$","").replace(",","").replace("USD1\xa0","").replace("USD","").strip()

  # Try to convert cleaned string to float, return None if conversion fails
  try:
    data_cleaned = float(data_cleaned)
  except ValueError:
    return None

  return str(data_cleaned)
