import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

b1 = a[0, :]
print(b1)
b1[0] = 99

print(a)

b2 = a.copy()
print(b2)