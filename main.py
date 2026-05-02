from cleaning_scrapping import mercado_libre_mx as ml_mx
from scrapping import Scrapping

mercado_libre_mx = Scrapping(ml_mx.url, ml_mx.html_element, ml_mx.html_class, ml_mx.cleaning_function)

