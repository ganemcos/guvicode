def chk_neighbour_for_0(lt,i,j):
        #checking horizantal and vertical elements
    if lt[i+1][j]== lt[i-1][j] == lt[i][j+1] == lt[i][j-1] == lt[i+1][j+1] == lt[i+1][j-1] == lt[i-1][j+1] == lt[i-1][j-1] == 0:
        return True
    return False

n = int(input())
l = []
for i in range(n):
    temp = list(map(int,input().split()))
    temp.insert(0,0)
    temp.append(0)
    l.append(temp)

zero = [0]*(n+2)
l.insert(0,zero)
l.append(zero)
c = 0
for i in range(0,n+2):
    for j in range(0,n+2):
        if i!=0 and j!=0 and l[i][j] == 1:
            # print(i,j)
            if chk_neighbour_for_0(l,i,j):
                c+=1
        # print(l[i][j],end = " ")
    # print("\n")
print(c)