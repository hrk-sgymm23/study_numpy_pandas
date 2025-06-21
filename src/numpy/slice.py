import numpy as np

data = np.array([1, 2, 3])
print(data[1]) # 2
print(data[0:2]) # [1, 2]
print(data[1:]) # [2, 3]
print(data[:2]) # [1, 2]
print(data[:]) # [1, 2, 3]
print(data[::2]) # [1, 3]
print(data[::-1]) # [3, 2, 1]

data2 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(data2[data2 < 5]) # [1, 2, 3, 4]
print(data2[data2 > 5]) # [6, 7, 8, 9, 10, 11, 12]

print(data2[data2%2==0]) # [ 2  4  6  8 10 12]
print(data2[(data2 > 2) & (data2 < 11)]) # [ 3  4  5  6  7  8  9 10]

fiveup = (data2 > 5) | (data2 == 5)
print(fiveup)
