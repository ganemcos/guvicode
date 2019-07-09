null = input()
l = list(map(int,input().split()))
b = False
for i in l:
    if l.count(i) > 1:
        b = True
        break
print(i if b else "unique")