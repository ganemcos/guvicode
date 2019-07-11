import math
l,d = [],[]
for i in range(4):
    l.append(list(map(int,input().split())))
# print("#"*50)
for i in range(4):
    for j in range(i+1,4):
        if l[i][0] == l[j][0]:
            # print(l[i],l[j])
            d.append(math.sqrt(pow((l[i][0]-l[j][0]),2)+pow((l[i][1]-l[j][1]),2)))

        if l[i][1] == l[j][1]:
            # print(l[i],l[j])
            d.append(math.sqrt(pow(l[i][0]-l[j][0],2)+pow(l[i][1]-l[j][1],2)))       

print("yes" if d.count(d[0]) == 4 else "no")