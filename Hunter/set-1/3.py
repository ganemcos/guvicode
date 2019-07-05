null =input()
li = input().split()
res = []
for i in range(len(li)):
    if str(i) == li[i]:
        res.append(li[i])
print(" ".join(res) if len(res) > 0 else "-1")