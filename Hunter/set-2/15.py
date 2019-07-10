null = input()
l = list(input().split())
st = max(l)
s = l.index(st)

for i in range(s,len(l)):
    if i < len(l)-1 :
        if l[i]>l[i+1]:
            print(l[i],end = " ")
    if i == len(l)-1:
        print(l[i])
print(st)