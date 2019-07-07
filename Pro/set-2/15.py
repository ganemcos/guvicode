# null = input()
# i = sorted(map(int,input().split()),reverse= True)
# for o in i:
#     print(o)

null = input()
l = list(map(int,input().split()))
bl = list(map(bin,l))
bls = sorted(bl,reverse = True)
print(*bls)
for i in bls:
    print(int(i,2))
