n,m = map(int,input().split())
l,ind = [],[]
for i in range(n):
    l.append(list(map(int,input().split())))

# checking for zero and making zer ele's index list
for i in range(n):
    for j in range(m):
        if l[i][j] == 0:
            ind.append([i,j])
# MAKING INDEX ROW COLOMS ZERO
for k in ind:
    r,c = k[0],k[1]
    for i in range(n):
        for j in range(m):
            if i == r:
                l[i][j] = 0
            if j == c:
                l[i][j] = 0
for i in l:
    print(*i,end = "\n")