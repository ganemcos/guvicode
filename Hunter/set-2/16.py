n ,k = map(int,input().split())
l = list(map(int,input().split()))
l.sort()
i =  l.index(k)
print(l[i-1],l[i+1],end = " ")
d1,d2 = l[i-2]-l[i],l[i+2]-l[i]
if d1 < d2:
    print(l[i-2])
else:
    print(l[i+2])