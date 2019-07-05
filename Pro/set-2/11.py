# from itertools import combinations as c
# import random as r
i = int(input())
# rl = []
# for i in range(i):
#     # rl.append(r.randint(1,1000000000000000000))
# # l = ["ga","ba","sa","ru"]
# comb = c(rl,2)
# d = 0
# for i in comb:
#     d+=1
# print(d)

# '''ncr'''


print(i//2*(i-1) if i%2 == 0 else i//2*(i))