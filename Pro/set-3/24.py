i = int(input())
a = [None]*i
def bintostr(i,a):
    if i < 1:
        a = list(map(str,a))
        print("".join(a))
    else:
        a[i-1] = 0
        bintostr(i-1,a)
        a[i-1] =1
        bintostr(i-1,a)


bintostr(i,a)