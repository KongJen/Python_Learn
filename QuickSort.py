#function partition
def partition(arr, l, r,cnt): 
    i = l
    j = r
    #chack l<r
    if l != r and l < r:
        p = arr[l]
        i = i+1
        #loop until i >= j
        while i <= j:
            #when arr[j] less than p and arr[i] more than p. swap arr[j] and arr[i]
            if arr[j] < p and arr[i] > p:
                cnt += 1
                arr[j], arr[i] = arr[i], arr[j]
                
            #repeat i <- i+1 until  > p 
            if not arr[i] > p:
                i += 1
            #repeat j <- j+1 until  > p 
            if not arr[j] < p:
                j -= 1
    #swap arr[l] and arr[j]
    cnt += 1
    arr[l], arr[j] = arr[j], arr[l]
    return j,cnt

#function quick_sort
def quick_sort(arr, l, r, cnt):

    if l < r:
        s,cnt = partition(arr, l, r, cnt)
        #quick sort left size
        arr,cnt = quick_sort(arr, l, s - 1, cnt)
        #quick sort right size
        arr,cnt = quick_sort(arr, s + 1, r, cnt)       

    return arr,cnt

#Put word "MONGKUT" in A
# A = "MONGKUT"
A = "KINGMONGKUT"
cnt = 0
#Create array 
arr = [i for i in A]
#Use function
sort_A,cnt = quick_sort(arr, 0, len(arr)-1, cnt)
#print A
print("Original String:",A)
#print sort A (join with string)
print("Sorted String:",''.join(sort_A))
print("Compare String:",cnt)