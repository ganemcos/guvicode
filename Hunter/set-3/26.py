n=int(input())
x=list(map(int,input().split()))
m=reversed(x)
print(*m,sep = "->")
