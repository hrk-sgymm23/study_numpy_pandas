import numpy as np

a = np.array([1,  2,  3,  4,  5,  6,  7,  8,  9, 10])

arr1 = a[3:8]
print(arr1) # [4 5 6 7 8]

a1 = np.array([[1, 1], [2, 2]])
a2 = np.array([[3, 3], [4, 4]])

print(a1)
print(a2)

a3 = np.vstack((a1, a2))
print('a3',a3)

a4 = np.hstack((a1, a2))
print('a4', a4)

x = np.arange(1, 25).reshape(2, 12)
print(x)

x1 = np.hsplit(x, 3)
print(x1)

x2 = np.hsplit(x, (3,4))
print(x2)
