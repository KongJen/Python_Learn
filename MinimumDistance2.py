import numpy as np
 
def Multilist(n):
    point = [];
    for i in range(n):
        for j in range(1):
            x = list(map(float, input().split()))
        point.append(x)  
    return point

n = int(input())
point = Multilist(n)
m = 999999
for i in range(n):
    for j in range(i+1,n):
            p1 = np.array([point[i][0],point[i][1],point[i][2]])
            p2 = np.array([point[j][0],point[j][1],point[j][2]])
            # print(p1,p2)
            squared_dist = np.sum((p1-p2)**2, axis=0)
            dst = np.sqrt(squared_dist)
            if( dst < m):
                m = dst
print("{:.4f}".format(m))
