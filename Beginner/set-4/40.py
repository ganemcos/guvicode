i = int(input())
b = 1
a,con = 0,0
t = True
while t:
    if con+1 == i:
        t = False
    print(b,end = " ")
    c = b
    b = a+b
    a = c
    con +=1
