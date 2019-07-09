null = input()
l = list(map(int,input().split()))
for i in range(len(l)):
    for j in range(len(l)):
        k = l[i]+l[j]
        if k in l and i<j<k:
            print(l[i],l[j],k)