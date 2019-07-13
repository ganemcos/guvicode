n = int(input())
l = list(map(int,input().split()))
p = [1]*n

for i in range(n):
    if i == 0 and l[i] > l[i+1]:
        p[i] += p[i+1]
    if i > 0 and l[i] > l[i-1]:
        p[i] += p[i-1]
print(sum(p))