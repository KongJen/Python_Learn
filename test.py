def get_permutation(string, i=0):

    if i == len(string)-1:   	 
        print("".join(string))
    else:
        for j in range(i, len(string)):

            words = [c for c in string]
   
            # swap
            words[i], words[j] = words[j], words[i]
   	 
            get_permutation(words, i + 1)

def m(n):
    a = []
    for i in range(1,n+1):
        a.append(i)
    return a


n =  int(input())
num = m(n)
print(get_permutation(''.join(map(str, num ))))