n = int(input())
l = list(map(int,input().split()))
count = 0
for i in range(n):
    for j in range(i,n):  
        for k in range(j,n):
            if l[i]<l[j]<l[k]:
                count+=1
print(count)
