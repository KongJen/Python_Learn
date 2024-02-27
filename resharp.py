import numpy as np

a = np.array([[1,2,3], [4,5,6]])
b = np.reshape(a,6)
c = np.reshape(a,(3,2))
d = np.reshape(a, 6, order='F')
e = np.reshape(a,(2,3))
print(b)
print("\n")
print(c)
print("\n")
print(d)
print("\n")
print(e)
