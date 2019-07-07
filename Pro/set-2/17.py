n , k = input().split()
k = int(k)
b = False
l = list(map(int,input().split()))
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]+l[j] == k:
            b = True
print("yes" if b else "no")