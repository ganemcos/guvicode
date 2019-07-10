import numpy as np
def chk_neighbour_for_0(lt,i,j):
        #checking horizantal and vertical elements
    if lt[i+1][j]== lt[i-1][j] == lt[i][j+1] == lt[i][j-1] == lt[i+1][j+1] == lt[i+1][j-1] == lt[i-1][j+1] == lt[i-1][j-1] == 0:
        return True
    return False

n = int(input())
l = []
for i in range(n):
    l.append(list(map(int,input().split())))
c = 0
l = np.pad(l,pad_width =1 ,mode ="constant",constant_values = 0 )
# print(*l,sep = "\n")
for i in range(0,n+1):
    for j in range(0,n+1):
        if i!=0 and j!=0 and l[i][j] == 1:
            # print(i,j)
            if chk_neighbour_for_0(l,i,j):
                c+=1
print(c)