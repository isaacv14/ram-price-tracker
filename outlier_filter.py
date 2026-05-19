import numpy as np

def OutlierFilter(data_array):
  # Calculate values at 35th and 95th percentiles
  lower_bound, upper_bound= np.percentile(data_array, [35, 95])

  # Filter out prices below the 35th percentile and above the 95th percentile
  filtered_array = [x for x in data_array if lower_bound <= x <= upper_bound]

  return filtered_array
