import string
d = dict(zip(string.ascii_letters,range(1,52)))
o  = ['d','h','o','n','i']
prod,rprod = 1,1
for i in o:
    prod*=d[i]
l = list(input())
for i in l:
    rprod*=d[i]
print("yes" if prod == rprod else "no")