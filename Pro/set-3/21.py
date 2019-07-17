num=int(input())
l = list(map(int,input().split()))
a1 = sum(l[:len(l)//2])/len(l[:len(l)//2])
a2 = sum(l[(len(l)//2)+1:])/len(l[(len(l)//2)+1:])
if a1 == a2:
    print("yes")
else:
    print("no")
