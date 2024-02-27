#function insertion_sort
def insertion_sort(arr):
    cnt = 0
    #loop for i=2 to n (in python start 0)
    for i in range(1, len(arr)): 
        #let val be arr[i]
        val = arr[i]
        cnt += 1
        #j is in font of i
        j = i-1
        #loop while check j>=0 and arr[i]>val
        while j >=0 and arr[j] > val : 
            #let arr[j+1] be arr[j] 
            arr[j+1] = arr[j] 
            cnt += 1
            #Take j to minus 1 to the next.
            j -= 1
        #when out loop let arr[j+1] be val
        arr[j+1] = val

    return arr,cnt

#Put word "MONGKUT" in A
# A = "MONGKUT"
A = "KINGMONGKUT"
#Create array 
arr = [i for i in A]
#Use function
sort_A, cnt = insertion_sort(arr)
#print A
print("Original String:",A)
#print sort A (join with string)
print("Sorted String:",''.join(sort_A))
print("Compare String:", cnt)