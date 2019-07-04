p= []
def prime(i):
    c = 0
    for j in range(2,i-1):
        if i%j == 0:
            c =1
            break
    if not c:
        p.append(i)

b ,en = map(int,input().split())

for k in range(b,en+1):
    prime(k)
print(len(p))