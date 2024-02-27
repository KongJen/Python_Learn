def EditDis(str1, str2, A, B):

    if A == 0:
        return B

    if B == 0:
        return A

    if str1[A-1] == str2[B-1]:
        return EditDis(str1, str2, A-1, B-1)
 
    return 1 + min(EditDis(str1, str2, A, B-1),EditDis(str1, str2, A-1, B),EditDis(str1, str2, A-1, B-1))
 
 
str1 = str(input())
str2 = str(input())
print (EditDis(str1, str2, len(str1), len(str2)))