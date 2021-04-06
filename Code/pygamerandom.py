from astropy.io import fits
import random as random
import numpy as np
import matplotlib.pyplot as plt

def objectR(amount):
	
	data = []
	#print(data)

	while amount > 0:
		num1 = random.randrange(1, 100, 1)
		num2 = random.randrange(1, 100, 1)
		num3 = random.randrange(1, 100, 1)
		num4 = random.randrange(1, 100, 1)
		amount = amount - 1
		#print(num1, num2, num3, num4)
		data.append([num1, num2, num3, num4])

	np.savetxt("int.csv", data, fmt='% 4d', delimiter=",")
	#print(data)


def argmax(ds):
	data = np.loadtxt(ds, delimiter=',', dtype= int)
	#print(data)
	np.savetxt("intR.csv", data, fmt='% 4d', delimiter=",")

	max = np.amax(data)
	print('Max value', max)
	
	argmax = np.argmax(data)
	print('Argmax', argmax)

	res = np.unravel_index(argmax, data.shape)
	print('Coordinates', res)

	# plt.imshow(data.T, cmap=plt.cm.viridis)
	# plt.colorbar()
	# plt.show()



def mean_fits(files):
	n = len(files)
	mean = ""
	if n > 0:
		hdulist = fits.open(files[0])
		data = hdulist[0].data
		hdulist.close()
		for i in range(1, n):
			hdulist = fits.open(files[i])
			data += hdulist[0].data
			hdulist.close()
			mean = data / n
		print(mean)


if __name__ == '__main__':
	#mean_fits(['Resources/M42/frame-g-006073-4-0063.fits'])
	
	try:
	  objectR(100)
	except:
		print('No Amount')
	try:
	  argmax('M42.csv') #M42.csv
	except:
		print('No Data')
		
	try:
	  mean_fits('M42.csv')
	except:
		print('No Files')

