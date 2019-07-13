n,q=map(int,input().split())
l=list(map(int,input().split()))
for i in range(q):
    a,b=map(int,input().split())
    sl = l[a-1:b]
    res = sl[0]
    for i in range(1,len(sl)):
        res = res ^ sl[i]
    print(res)
    
