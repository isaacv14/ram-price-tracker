url = "https://www.amazon.com/b?node=172500"
html_element = "span"
html_class = "a-price-whole"

def cleaning_function(price_text):
  """Clean price text specific to Amazon US"""
  # Remove thousand separators
  data_cleaned = price_text.replace(",","").replace(".","").strip()

  return str(data_cleaned)
