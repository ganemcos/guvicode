null = input()
l = list(map(int,input().split()))
gsum = 0
step= []
if len(set(l)) == 1:
    print(0)
else:
    for i in range(len(l),0,-1):
        g = sum(l[:i])
        step.append(g)
    step.remove(max(step))
    print(sum(step))