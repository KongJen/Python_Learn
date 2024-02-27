import numpy as np
from decimal import Decimal

def calc_distance(p1, p2): 
    return np.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)

def minimum( m, dst):
    if m > dst:
        return dst
    else:
        return m

lst = []
m = 99999
n = int(input())
for i in range(0, n):
    p = []
    for j in range(1):
        x,y,z = map(Decimal, input().split())
        p.append(x)
        p.append(y)
        p.append(z)
    lst.append(p)  
for i in range(n):
    for j in range(i+1,n):
        dst = calc_distance(lst[i], lst[j])
        m = minimum(m,dst)
print("{:.4f}".format(m))