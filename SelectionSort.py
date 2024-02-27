#function selection_sort
def selection_sort(arr):
    cnt=0
    #loop for i=1 to n-1 (in python start 0)
    for i in range(len(arr)-1): 
        #let min be i
        cnt += 1 
        min = i
        #loop for j=i+1 to n
        for j in range(i+1,len(arr)):
            cnt += 1 
            #when arr[j] lower than arr[min]. let min to j
            if(arr[j] < arr[min]):
                min = j
        #swap arr[i] to arr[min] and arr[min] to arr[i] 
        arr[i],arr[min] = arr[min],arr[i]       
    return arr,cnt

#Put word "MONGKUT" in A
# A = "MONGKUT"
A = "KINGMONGKUT"
#Create array 
arr = [i for i in A]
#Use function
sort_A,cnt = selection_sort(arr)
#print A
print("Original String:",A)
#print sort A (join with string)
print("Sorted String:",''.join(sort_A))
print("Compare String:",cnt)