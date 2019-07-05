def editDistance(s1,s2,m,n):
    if m == 0:
        return n

    if n == 0:
        return m

    if s1[m-1] == s2[n-1]:
        return editDistance(s1,s2,m-1,n-1)
    
    return 1 + min(editDistance(s1,s2,m,n-1),
                (editDistance(s1,s2,m-1,n)),
                (editDistance(s1,s2,m-1,n-1)))

s1,s2 = input().split()
s1len,s2len =len(s1),len(s2) 
print(editDistance(s1,s2,s1len,s2len))