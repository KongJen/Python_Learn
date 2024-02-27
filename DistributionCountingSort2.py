#function distribution_counting_sort
def distribution_counting_sort(arr):
    #count array is ASCII decimal
    count = [0 for i in range(256)]
    out = [0 for i in range(len(arr))]
    #count of each character
    for i in arr:
        count[ord(i)] += 1

    #build new array by position new array is i-1
    for i in range(256):
        count[i] += count[i-1]   


    #build output character array
    for i in range(len(arr)):
        out[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1
    # Copy the out array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        arr[i] = out[i]

    return arr

#Put word "MONGKUT" in A
A = "MONGKUT"
# A = "KINGMONGKUT"
#Create array 
arr = [i for i in A]
#Use function
sort_A = distribution_counting_sort(arr)
#print A
print("Original String:",A)
#print sort A (join with string)
print("Sorted String:",''.join(sort_A))