# Write your calc_stats function here.
import numpy as np
import timeit

def calc_stats(data):
	data = np.loadtxt(data, delimiter=',')
	mean = round(np.sum(data)/data.size, 1)
	median = round(np.median(data), 2)
	stats = [mean, median]
	return stats

def calc_stats2(data):
	data = np.loadtxt(data, delimiter=',')
	mean = np.round(np.mean(data), 1)
	median = np.round(np.median(data), 1)

	return mean, median

def mean_datasets(files):
  n = len(files)
  if n > 0:
    data = np.loadtxt(files[0], delimiter=',')
    for i in range(1,n):
      data += np.loadtxt(files[i], delimiter=',')
    
    print(data)
    round = 1
    mean = np.round(data/n, round)
     
    return mean
  

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
	# Run your `calc_stats` function with examples:
	mean = calc_stats2('data.csv')
	md = mean_datasets(['data1.csv', 'data2.csv', 'data3.csv'])

	print(mean)
	print(md)
	print(md.ndim)
	print(timeit.timeit(lambda: mean))

