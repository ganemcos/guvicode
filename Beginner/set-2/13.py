n = int(input())
c = 0
for i in range(2,n-1):
    if n%i == 0:
        c = 1
        break
print("yes" if not c else "no")