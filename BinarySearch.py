def binary_search(arr, l, h, x):
	if h >= l:
		mid = (h + l) // 2
		if arr[mid] == x:
			return mid
		elif arr[mid] > x:
			return binary_search(arr, l, mid - 1, x)
		else:
			return binary_search(arr, mid + 1, h, x)
	else:
		return -1

L = []
n = int(input())
k = int(input())
for i in range(0, n):
    ele = int(input())

    L.append(ele) 
for j in range(0 , k):
    s = int(input())

    result = binary_search(L, 0, len(L), s)
    print(result)
