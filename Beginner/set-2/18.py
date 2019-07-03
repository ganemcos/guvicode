
def arm(i):
    n = int(i)
    i = list(map(int,list(i)))
    for k in range(10):
        su = 0
        s = []
        for g in i:
            s.append(pow(g,k))
        su= sum(s)
        if su == n:
            print(n,end=" ")
            break

b ,e = map(int,input().split())
for h in range(b+1,e):
    arm(str(h))