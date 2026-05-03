from scipy import stats
import numpy as np
from cleaning_scrapping import mercado_libre_mx as ml_mx
from scrapping import Scrapping
from outlier_filter import OutlierFilter

mercado_libre_mx = Scrapping(ml_mx.url, ml_mx.html_element, ml_mx.html_class, ml_mx.cleaning_function)

ml_mx_filtered = OutlierFilter(mercado_libre_mx)

print(mercado_libre_mx)