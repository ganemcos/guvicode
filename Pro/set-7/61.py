import string
lw = list(string.ascii_lowercase)

l1 = list(input())
l2 = list(input())
l3 = []
for i in range(len(l1)):
    tw = lw.index(l1[i])+lw.index(l2[i])+1
    if tw < 25:
        print(lw[tw],end = "")
    else:
        print(lw[tw-26],end = "")
