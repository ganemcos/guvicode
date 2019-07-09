n = input()
a = set(map(int,input().split()))
b = set(map(int,input().split()))
print("YES" if b.issubset(a) else "NO")