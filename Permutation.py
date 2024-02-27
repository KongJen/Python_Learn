from xmlrpc.client import TRANSPORT_ERROR


L_to_R = True
R_to_L = False

def searcharr(a,n,m):
    for i in range (0,n):
        if a[i] == m:
            return i+1

def getm(a,d,n):
    mp = 0
    m = 0
    for i in range (0,n):
        if d[a[i]-1] == R_to_L and i != 0:
            if a[i] > a[i-1] and a[i] > mp:
                m = a[i]
                mp = m
        
        if d[a[i]-1] == L_to_R and i != n-1:
            if a[i] > a[i+1] and a[i] > mp:
                m = a[i]
                mp = m

    if m == 0 and mp == 0:
        return 0
    else:
        return m

def printPer(a,d,n):
    m =getm(a,d,n)
    p = searcharr(a,n,m)

    if (d[a[p-1]-1] == R_to_L):
        a[p-1], a[p-2] = a[p-2], a[p-1]
    elif (d[a[p-1]-1] == L_to_R):
        a[p-1], a[p] = a[p], a[p-1]

    for i in range (0,n):
        if a[i] > m:
            if d[a[i]-1] == L_to_R:
                d[a[i]-1] = R_to_L
            elif d[a[i]-1] == R_to_L:
                d[a[i]-1] = L_to_R

    for i in range(0,n):
        a.append(a[i])
    a.append[" "]


def fact(n):
    r = 1
    for i in range (1,n+1):
        r = r*i
    return r


def permutation(n):
    a = [n]
    d = []

    for i in range (0,n):
        a[i] = i+1;
        a.append(a[i])
    a.append("\n")

    for i in range (0,n):
        d[i] = R_to_L

    for i in range(1,fact(n)):
        printPer(a,d,n)


n = int(input())
if n > 0:
    permutation(n)