url = "https://www.amazon.com/b?node=172500"
html_element = "span"
html_class = "a-price-whole"

def cleaning_function(price_text):
  """Clean price text specific to Amazon US"""
  # Remove thousand separators
  data_cleaned = price_text.replace(",","").replace(".","").strip()
  
  # Try to convert cleaned string to float, return None if conversion fails
  try:
    data_cleaned = float(data_cleaned)
  except ValueError:
    return None
  
  return str(data_cleaned)
