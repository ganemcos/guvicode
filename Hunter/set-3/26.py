n=int(input())
l=list(map(int,input().split()))
m=reversed(l)
print(*m,sep = "->")
