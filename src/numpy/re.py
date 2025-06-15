import numpy as np

a = np.arange(6)

print(a) # [0 1 2 3 4 5]

print(a.reshape(3, 2)) # [[0 1] [2 3] [4 5]]

print(a.reshape(2, 3)) # [[0 1 2] [3 4 5]]

print(a.reshape(2, 3, 1)) # [[[0] [1] [2]] [[3] [4] [5]]] 

print(np.reshape(a, shape=(1, 6), order='C')) # [[0 1 2 3 4 5]]