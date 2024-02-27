def linearSearch(L, n, k):

    # Going through array sequencially
    for i in range(0, n):
        if (L[i] == k):
            return i
    return -1

L = []
n = int(input())
for i in range(0, n):
    ele = int(input())

    L.append(ele) 
k = int(input())
result = linearSearch(L, n, k)
print(result)