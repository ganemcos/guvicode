rlen,r = input().split()
rlen,r = int(rlen),int(r)
b = []
for t in range(r):
    temp = list(map(int,input().split()))
    temp.sort()
    b.append(temp)

for i in range(rlen):
    t = []
    for j in range(r):
        t.append(b[j][i])
        # print(b[j][i],end = " ")
    # print('\n')
    t.sort()
    for j in range(r):
        b[j][i] = t[j]
        # print(b[j][i])

for i in range(r):
    print(*b[i])
