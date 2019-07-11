i = int(input())
l = list(map(int,input().split())) 
for i in range(len(l)):
    prod = 1
    for j in range(len(l)):
        if j != i:
            prod*= l[j]
    print(prod,end = " ")
    
