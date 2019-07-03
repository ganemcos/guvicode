def prime(i):
    c = 0
    for j in range(2,i-1):
        if i%j == 0:
            c =1
            break
    if not c:
        print(i,end=" ")

b ,e = map(int,input().split())
l =[]
for k in range(b+1,e):
    prime(k)
