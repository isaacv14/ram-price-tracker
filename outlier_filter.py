import numpy as np

def OutlierFilter(data_array):
  sorted_array = sorted(data_array)

  # Calculate values at 35th and 95th percentiles
  lower_number, upper_number= np.percentile(sorted_array, [35, 95])

  # Filter out prices below the 35th percentile and above the 95th percentile
  filtered_array = filter(lambda x: (x > lower_number and x < upper_number), sorted_array)

  return list(filtered_array)
