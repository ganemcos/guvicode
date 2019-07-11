i = int(input())
l = list(map(int,input().split())) 
for i in range(len(l)):
    prod = 1
    for j in l:
        if j != l[i]:
            prod*= j
    print(prod,end = " ")
    
