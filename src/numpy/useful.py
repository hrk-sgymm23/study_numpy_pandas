import numpy as np

data = np.array([1.0, 2.0])
print(data.max())
print(data.min())
print(data.sum())

a = np.array([[0.45053314, 0.17296777, 0.34376245, 0.5510652],
              [0.54627315, 0.05093587, 0.40067661, 0.55645993],
              [0.12697628, 0.82485143, 0.26590556, 0.56917101]])

print(a.sum())
print(a.min())

print(a.min(axis=0))