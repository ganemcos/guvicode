import math as m
s = list(input())
c = 0 
for i in range(m.floor(len(s)/2)):
    if s[i] != s[len(s)-1-i]:
        # print("no")
        # break
        continue
    else:
        c+=2
print("yes" if c+1 == len(s) else "no")