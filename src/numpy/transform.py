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

arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
reversed_arr = np.flip(arr_2d)
print(reversed_arr)

reversed_arr_columns = np.flip(arr_2d, axis=1)
print(reversed_arr_columns)

arr_2d[1] = np.flip(arr_2d[1])
print(arr_2d)

arr_2d[:,1] = np.flip(arr_2d[:,1])
print(arr_2d)