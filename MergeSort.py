#function merge_sort
def merge_sort(arr, cnt):
    
    #length of arr must more than 1
    if len(arr) > 1:
        #Divide half arr into the front half(L) and the back half(R).
        m = len(arr)//2
        L = arr[:m]
        R = arr[m:]
        #Divide until length remains 1
        merge_sort(L,cnt)
        merge_sort(R,cnt)

        i = j = k = 0

        #With respect to L and R, which side is less will be put into arr.
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                cnt += 1
                i += 1
            else:
                arr[k] = R[j]
                cnt += 1
                j += 1
            k += 1

        #Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            cnt += 1
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            cnt += 1
            j += 1
            k += 1
    return arr,cnt

#Put word "MONGKUT" in A
# A = "MONGKUT"
A = "KINGMONGKUT"
#Create array 
arr = [i for i in A]
cnt = 0
#Use function
sort_A, cnt = merge_sort(arr, cnt)
#print A
print("Original String:",A)
#print sort A (join with string)
print("Sorted String:",''.join(sort_A))
print("Compare String:", cnt)