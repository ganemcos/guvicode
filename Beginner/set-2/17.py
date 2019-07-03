def arm(i):
    found =0
    n = int(i)
    i = list(map(int,list(i)))
    for k in range(10):
        su = 0
        s = []
        for g in i:
            s.append(pow(g,k))
        su= sum(s)
        if su == n:
            found =1
    print("yes" if found else "no")
input = input()
arm(input)