l = list(input())
big = 0
for i in range(len(l)):
    temp = l[i:len(l)]
    stemp = list(reversed(temp))
    # print(temp,stemp)abcd
    if temp == stemp:
        if big < len(stemp):
            big  = len(stemp)
for i in range(len(l)):
    temp = l[:len(l)-i]
    stemp = list(reversed(temp))
    # print(temp,stemp)
    if temp == stemp:
        if big < len(stemp):
            big  = len(stemp)
print(len(l)-big)