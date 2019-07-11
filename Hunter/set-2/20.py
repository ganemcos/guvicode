def isprime(num):
    if num == 1:
        return False
    for i in range(2,num):
        if num%i == 0: 
            return False
    return True

b,e = map(int,input().split())
count = 0

for i in range(b,e+1):
    m = bin(i).count('1')
    # print(i,m,bin(i))
    if isprime(m):
        count+=1
print(count)