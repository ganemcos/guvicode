x= list(input())
le = 0
a= []
for i in range(len(x)):
    t = x[:i]
    rt = list(reversed(t))
    if t != rt:
        if len(t) > le:      
            le = len(t)
            a = t
            #print("p",t,le)
for i in range(len(x)):
    t = l[i:]
    rt = list(reversed(t))
    if t != rt:
        if len(t) > le:
            le = len(t)
            a = t
            #print("p",t,le)

print("".join(a))
