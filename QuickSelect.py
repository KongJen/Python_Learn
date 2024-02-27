
def LomutoPartition(arr, l, r,cnt): 
    p=arr[l]
    s=l
    for i in range (l,r):
        if arr[i] < p:
            arr[s],arr[i] = arr[i],arr[s]  
            s += 1
            cnt += 1
            
    cnt += 1
    arr[l],arr[s] = arr[s],arr[l]  
    return s,cnt


def QuickSelect(arr, l, r, k, cnt):
    if (k > 0 and k <= r-l+1):
        s,cnt = LomutoPartition(arr,l,r,cnt)
        if s-l == k-1:
            return arr[s],cnt
        elif s-l > k-1:
            return QuickSelect(arr,l,s-1,k,cnt)
        else:
            return QuickSelect(arr,s+1,r,k-s+l-1,cnt)
    

arr = [33,29,16,28,32,34]
k = 4
cnt = 0
print("Original String:",arr)
#Use function
sort_A,cnt = QuickSelect(arr, 0, len(arr)-1, k, cnt)
print("Kth smaller:",sort_A)
print("Compare String:",cnt)