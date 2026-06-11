import numpy as np
from scraping import Scraping, CrawlbaseScrape, PlayWrightScraping
from outlier_filter import OutlierFilter
from sites import mercado_libre_mx as ml_mx
from sites import amazon_us as am_us
from sites import ebay_us as eb_us

# Configure sites to scrape (URL, HTML element, CSS class, cleaning function)
sites = [
  #Scraping(ml_mx.url, ml_mx.html_element, ml_mx.html_class, ml_mx.cleaning_function), --- SCRAPING DOESN'T WORK, FIX LATER ---
  CrawlbaseScrape(am_us.url, am_us.html_element, am_us.html_class, am_us.cleaning_function),
  PlayWrightScraping(eb_us.url, eb_us.html_element, eb_us.html_class, eb_us.cleaning_function)
]

# Scrape and filter outliers from each site
total_data = []

for site in sites:
  clean_data = OutlierFilter(site)
  total_data.append(clean_data)

# Calculate average price from filtered data
np_average = np.mean(total_data)

print(f"Average Price: {np_average}")
