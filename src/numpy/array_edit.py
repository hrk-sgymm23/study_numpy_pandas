import numpy as np

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])

print(np.sort(arr)) # [1 2 3 4 5 6 7 8]
print(np.sort(arr)[::-1]) # [8 7 6 5 4 3 2 1]

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(np.concatenate((a, b))) # [1 2 3 4 5 6 7 8]

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6]])

z = np.concatenate((x, y), axis=0) # [[1 2] [3 4] [5 6]]
print(z)

z_deleted = np.delete(z, 1, axis=0) # [[1 2] [5 6]]
print(z_deleted)

z_deleted = np.delete(z, 1, axis=1) # [[1] [3] [5]]
print(z_deleted)





