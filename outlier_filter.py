import numpy as np

def OutlierFilter(data_array):
  sorted_array = sorted(data_array)

  # Calculate number at 35% & 85% position
  lower_number, upper_number= np.percentile(sorted_array, [35, 85])

  # filtering numbers bellow 35% and above 85%
  filtered_array = filter(lambda x: (x > lower_number and x < upper_number), sorted_array)

  return list(filtered_array)
