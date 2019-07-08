i = int(input())
l = []
for j in range(i):
    temp = list(map(int,input().split()))
    l.extend(temp)
l.sort()
print(*l)
    
