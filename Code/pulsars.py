from statistics import mean
fluxes = [23.3, 42.1, 2.0, -3.2, 55.6]
m = mean(fluxes)
print('Statistics mean', m)

fluxes = [23.3, 42.1, 2.0, -3.2, 55.6]
m = sum(fluxes)/len(fluxes)
print('Manual mean', m)

#####################################################################
# Write your calculate_mean function here.
def calculate_mean(data):
  mean = sum(data)/len(data)
  return mean

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calculate_mean` function with examples:
  mean = calculate_mean([1,2.2,0.3,3.4,7.9])
  print(mean)
  
#####################################################################

import numpy as np
fluxes = np.array([23.3, 42.1, 2.0, -3.2, 55.6])
m = np.mean(fluxes)
print(m)

import numpy as np
fluxes = np.array([23.3, 42.1, 2.0, -3.2, 55.6])
print(np.size(fluxes)) # length of array
print(np.std(fluxes))  # standard deviation


a = np.array([2, 1, 5, 7, 4, 6, 8, 14, 10, 9, 18, 20, 22])

import matplotlib.pyplot as plt

plt.plot(a)

