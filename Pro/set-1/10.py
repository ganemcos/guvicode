null = input()
l = list(map(int,input().split()))
gsum = 0
for i in range(1,len(l)):
    for x in l[:i]:
        if x<l[i]:
            gsum+=x
print(gsum)