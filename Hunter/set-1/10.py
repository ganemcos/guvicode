n = input()
a = set(map(int,input().split()))
b = set(map(int,input().split()))
print("Yes" if b.issubset(a) else "No")