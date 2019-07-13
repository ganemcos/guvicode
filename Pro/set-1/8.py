import math
n , k = map(int,input().split())
l = list(map(int,input().split()))
for i in range(k):
    b,e = map(int,input().split())
    gcd = l[b-1]
    if b == e:
        print(l[i])
    else:
        for i in range(b,e):
            gcd = math.gcd(gcd, l[i])
    print(gcd)