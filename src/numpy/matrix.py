import numpy as np

data = np.array([[1, 2], [3, 4], [5, 6]])
print(data)

print(data[0, 1])
print(data[1:3])

print(data.max())
print(data.min())
print(data.sum())

data = np.array([[1, 2], [5, 3], [4, 6]])
print(data)

print(data.max(axis=0))
print(data.min(axis=1))

data = np.array([[1, 2], [3, 4], [5, 6]])
ones_row = np.array([[1, 1]])
print(data + ones_row)