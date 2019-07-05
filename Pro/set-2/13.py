n,q = map(int,input().split())
n = list(map(int,input().split()))
for i in range(q):
    b ,e = map(int,input().split())
    res = min(n[b-1:e])
    # print(*n[b-1:e])
    print(res)