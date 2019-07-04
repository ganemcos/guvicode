def progresssion(n,a,d):
    t =(n/2)*((2*a)+(n-1)*d)
    return int(t)

i = list(map(int,input().split()))
print(progresssion(i[0],i[1],i[2]))