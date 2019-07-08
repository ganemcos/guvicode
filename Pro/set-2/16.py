null = input()
l = list(map(int,input().split()))
choclate =0 
while len(set(l)) != 1:
    print(len(set(l)))
    print(l,choclate)
    for i in range(len(l)):
        if l[i] != 0:
            choclate+=1
            l[i] -=1 
    l.remove(0)
print(choclate)


#todo