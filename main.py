import numpy as np
from cleaning_scrapping import mercado_libre_mx as ml_mx
from scrapping import Scrapping
from outlier_filter import OutlierFilter
import time

# Track execution time
inicio = time.time()

# Configure sites to scrape (URL, HTML element, CSS class, cleaning function)
sites = [
  Scrapping(ml_mx.url, ml_mx.html_element, ml_mx.html_class, ml_mx.cleaning_function),
]

# Scrape and filter outliers from each site
total_data = []

for site in sites:
  clean_data = OutlierFilter(site)
  total_data.append(clean_data)

# Calculate average price from filtered data
np_average = np.mean(total_data)
