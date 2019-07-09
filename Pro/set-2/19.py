l = int(input())
l = []
for j in range(k):
    temp = list(map(int,input().split()))
    l.extend(temp)
l.sort()
print(*l)
    
