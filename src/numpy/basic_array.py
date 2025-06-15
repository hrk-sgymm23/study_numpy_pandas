import numpy as np

print(np.zeros(2)) # [0. 0.]
print(np.zeros((2, 3))) # [[0. 0. 0.] [0. 0. 0.]]

print(np.ones(2)) # [1. 1.]
print(np.ones((2, 3))) # [[1. 1. 1.] [1. 1. 1.]]

x = np.ones(2, dtype=np.int64)
print('x', x) # [1 1]

print(np.empty(2)) # [1., 1.]

print(np.arange(4)) # [0 1 2 3]

print(np.arange(2, 9, 2)) # [2 4 6 8]

print(np.linspace(0, 10, num=5)) # [ 0.  2.5  5.  7.5 10.]

print(np.linspace(0, 10, num=5, endpoint=False)) # [0. 2. 4. 6. 8.]