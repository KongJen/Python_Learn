def selection_sort(arr):
    #loop for i=1 to n-1 (in python start 0)
    for i in range(len(arr)-1): 
        #let min be i
        min = i
        #loop for j=i+1 to n
        for j in range(i+1,len(arr)):
            #when arr[j] lower than arr[min]. let min to j
            if(arr[j] < arr[min]):
                min = j
        #swap arr[i] to arr[min] and arr[min] to arr[i] 
        arr[i],arr[min] = arr[min],arr[i]       
    return arr


def PresortUniqueElement(arr,l,n):
    arr = selection_sort(arr)
    i = 0
    f = 0
    while i <= n-1:
        length = 1
        value = arr[i]
        while i+length<=n-1 and arr[i+length] == value:
            length = length+1
        if length > f:
            f = length
            mvalue = value
        i = i+length

    return mvalue



arr = [3,13,1,6,5,8,13,9,8]
print(PresortUniqueElement(arr,0,len(arr)))