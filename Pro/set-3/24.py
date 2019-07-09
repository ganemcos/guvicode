i = int(input())
a = [None]*i
b = []
num = []
def bintostr(i,a):
    if i < 1:
        a = "".join(list(map(str,a)))
        b.append(a)
    else:
        a[i-1] = 0
        bintostr(i-1,a)
        a[i-1] =1
        bintostr(i-1,a)

bintostr(i,a)
# print(b)
for i in range(len(b)):
    num.append(int(b[i],2))
num.sort()
# print(num)
res = []
for i in range(len(b)):
    res.append(bin(num[i])[2:])
# print(*res)
res = list(map(str,res))
fres = []
blen = (len(b[-1]))
fres= map(lambda x: x.zfill(blen), res)
print(*fres,sep="\n")

    #todo only one attempt