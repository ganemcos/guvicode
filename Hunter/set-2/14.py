from itertools import permutations as c
l = list(input())
lc = list(c(l))
for i in lc:
    print("".join(i))