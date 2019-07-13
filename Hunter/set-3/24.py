n,k=map(int,input().split())
x=list(map(int,input().split()))
a=0
for i in range(0,n):
    for j in range(1,n):
        if x[i]+x[j]==k and i!=j:
            a=1
            break
print("YES" if a else "NO")
