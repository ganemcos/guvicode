l = list(map(int,input().split()))
tot,n1,n2,flag = l[0],l[1],l[2],0
for i in range(1,10):
    if (n1*i+n2*i) == tot:
        flag = 1
        break
print("YES" if flag else "NO")