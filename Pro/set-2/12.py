n,q = map(int,input().split())
n = list(map(int,input().split()))
print(n)
for i in range(q):
    b ,e = map(int,input().split())
    res = sum(n[b-1:e])
    # print(*n[b-1:e])
    print(res)