# 標準の配列とNumpyの配列の違い
import numpy as np

standard_array = [1, 2, 3, 4, 5, 6]
numpy_array = np.array([1, 2, 3, 4, 5, 6])

print(standard_array)
print(numpy_array)

a = standard_array[3:]
a[0] = 100
print('slice_standard_array', a) # [1, 2, 3, 4, 5, 6]
print('standard_array', standard_array) # [1, 2, 3, 100, 5, 6]

b = numpy_array[3:]
b[0] = 100
print('slice_numpy_array', b) # [100, 5, 6]
print('numpy_array', numpy_array) # [1, 2, 3, 100, 5, 6]


matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('matrix', matrix)
print('matrix[1][3]', matrix[1][3]) # 8