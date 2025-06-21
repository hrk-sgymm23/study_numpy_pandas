import numpy as np

data = np.array([1, 2])
ones = np.ones(2, dtype=int)

a = data + ones
print(a)

b = data - ones
print(b)

c = data * ones
print(c)

d = data / ones
print(d)

a = np.array([1, 2, 3, 4])
print(a.sum())

# 軸で合計できる
b = np.array([[1, 1], [2, 2]])
print(b.sum(axis=0))
print(b.sum(axis=1))

