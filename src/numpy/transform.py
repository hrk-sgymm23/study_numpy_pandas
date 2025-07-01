import numpy as np

data = np.array([[1, 2], [3, 4], [5, 6]])

print(data.reshape(2, 3))
print(data.reshape(3, 2))

arr = np.arange(6).reshape((2, 3))
print(arr)

print(arr.transpose())  

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
reversed_arr = np.flip(arr2)

print(reversed_arr)
