import numpy as np
def chk_neighbour_for_0(lt,i,j):
        #checking horizantal and vertical elements
    # if (lt[i+1,j] and lt[i-1,j] and lt[i,j+1] and lt[i,j-1]) == '0':
    #     ib = True

    #     #checking diagnal elements 
    # if (lt[i+1,j+1] and lt[i+1,j-1] and lt[i-1,j+1] and lt[i-1,j+1]) == '0':
    #     ij = True



    # if ib and ij:
    #     return True
    # else:
    #     return False

n = int(input())
l = []
for i in range(n):
    l.append(list(input().split()))
c = 0
for i in range(n):
    for j in range(n):
        if chk_neighbour_for_0(l,i,j):
            c+=1
print(c)