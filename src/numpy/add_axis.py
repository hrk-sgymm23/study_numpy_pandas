import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print(a.shape) # (6,)

a2 = a[np.newaxis, :]
print(a2.shape) # (1, 6)

a3 = np.array([1, 2, 3, 4, 5, 6])
print(a3.shape) # (6,)
a4 = np.expand_dims(a3, axis=0)
print(a4.shape) # (1, 6)
a5 = np.expand_dims(a3, axis=1)
print(a5.shape) # (6, 1)


