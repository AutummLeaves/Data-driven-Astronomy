import numpy as np;

a = [1,2,3]

a = np.array([1,2,3])
b = np.array([2,2,2])
d = np.array([[1,2,3,10,4],[1,2,3,10,4],[1,2,3,10,4]])

c = a * b

#print(a * b)
#print(c)
#print(a)
print(d)
# Get Dimention
print(d.ndim)
# Get Shape
print(d.shape)
# Get Type
print(d.dtype)
# Get Size
print(d.itemsize)
# Get Total Size
print("test", d.size * a.itemsize)
print(d.nbytes)

#############################################

# Get Specific element [r, c]
print(d[2, 1])
print(d[2, -1])
# Get specific Row
print(d[2, :])
# Get specific Column
print(d[:, 2])
# Get [startindex:endindex:stepsize]
print(d[0, 0:3:1])
#############################################

# Change 1 element
d[1, 0] =  20
print(d[:, :])
# Change row or colum
d[0, :] = 5
print([d])
d[2, :] = [1, 2 ,3, 4, 5]
print([d])

# All 0s Matrix
matrix0 = np.zeros((5, 5))
print(matrix0)
# All 1s Matrix
matrix1 = np.ones((2, 2))
print(matrix1)
# Any Number Matrix
matrixfull = np.full((2, 2), 5)
print(matrixfull)

# Any Number From Array shape
matrixshape0 = np.full_like(d, 5)
print(matrixshape0)
matrixshape1 = np.full(d.shape, 1)
print(matrixshape1)


