n,q=map(int,input().split())
l=list(map(int,input().split()))
for i in range(q):
    a,b=map(int,input().split())
    sl = l[a-1:b]
    out = sl[0]
    for i in range(1,len(sl)):
        out = out ^ sl[i]
    print(out)
    
