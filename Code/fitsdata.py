from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import timeit

def map(image):
	hdulist = fits.open(image)
	print(hdulist.info())
	print('Fits ', hdulist)

	imageArray = hdulist[0].data
	#np.savetxt("M42.csv", data, delimiter=",")

	for i in imageArray:
		print(i)

	print(imageArray)

	print('dimention ',imageArray.ndim)
	print('Shape ', imageArray.shape)
	print('itemsize ',imageArray.itemsize)
	print('nbytes ',imageArray.nbytes)

	print('Max axis 0 ', np.amax(imageArray, axis = 0))
	print('Max axis 1 ', np.amax(imageArray, axis = 1))


	# Plot the 2D image data
	plt.imshow(imageArray.T, cmap=plt.cm.viridis)
	plt.colorbar()
	plt.xlabel('x-pixels')
	plt.ylabel('y-pixels')

	plt.show()


def load_fits(filename):

	hdulist = fits.open(filename)
	data = hdulist[0].data
	print(data.ndim)

	arg_max = np.argmax(data)  
	max_pos = np.unravel_index(arg_max, data.shape)
	print('Arg Max', arg_max)
	print('Data Shape',data.shape)
	print('Max Pos',max_pos)
	  
	return max_pos


	

if __name__ == '__main__':
	
	load_fits('C:\\Google Drive\\Coursera\\Data-driven Astronomy\\Code\\Resources\\M42\\frame-g-006073-4-0063.fits')

	try:
		timeit.timeit(map('C:\\Google Drive\\Coursera\\Data-driven Astronomy\\Code\\Resources\\M42\\frame-g-006073-4-0063.fits'))
		
	except:
		print("No Map")