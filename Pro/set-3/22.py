null = int(input())
esum,osum = 0,0
l = list(map(int,input().split()))
for i in range(null):
    if i%2 == 0:
        esum+=l[i]
    else:
        osum+=l[i]
print(esum , osum)


#todo for input
# 5
# 1 5 1 5 9