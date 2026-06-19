url = "https://www.bestbuy.com/site/computer-cards-components/computer-memory/abcat0506000.c?id=abcat0506000&intl=nosplash"
html_element = "span"
html_class = "sr-only"

def cleaning_function(price_text):
  """Clean price text specific to Best Buy US"""
  # Remove thousand separators
  data_cleaned = price_text.replace(",","").replace("$","").strip()
  try:
    data_cleaned = float(data_cleaned)
  except ValueError:
    return None

  return str(data_cleaned)
