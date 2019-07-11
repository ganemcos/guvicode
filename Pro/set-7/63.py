from itertools import permutations as c
l = list(input())
# big = 0
temp = []
# for i in range(len(l)):
#     if l[i] not in temp:
#         l.append(l[i])
#         print(temp)
#     else:
#         if big < len(temp):
#             big = len(temp)
# print(big)
for i in range(2,len(l)):
    lc = list(c(l,i))
    for i in lc:
        print(len(i),set(i))
        if len(i) == set(i):
            temp.append(len(i))
print(temp)