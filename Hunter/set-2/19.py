n,k = input().split()
n = int(n)
l = []
for i in range(n):
    l.append(set(map(int,input().split())))
print(*set.intersection(*l))