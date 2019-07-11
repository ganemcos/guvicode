n,k=map(int,input().split())
l=list(map(int,input().split()))
a=0
for i in range(0,n):
    for j in range(1,n):
        if l[i]+l[j]==k and i!=j:
            a=1
            break
print("YES" if a else "NO")
