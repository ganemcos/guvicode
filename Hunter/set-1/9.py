from itertools import combinations as c
n = int(input())
l = list(map(int,input().split()))
lc = list(c(l,2))
suml = [i[0]+i[1] for i in lc]
# print(lc,suml,sep = "\n")
# print(min(suml))
b =False
min_index = suml.index(min(suml))
zerocount = suml.count(0)
if zerocount == 1:
    zero_index = suml.index(0)
    print(*lc[zero_index])
else:
    print(*lc[min_index])
