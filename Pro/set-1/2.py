from itertools import combinations
num ,x = input().split()
x = int(x)
snum = []
comb = combinations(num,len(num)-x)
for i in comb:
    snum.append("".join(i))
print(min(snum))


# def smalnum_aft_k_del(list1,del_num_count):
#     dl= []
#     m = sorted(list1)
#     if m == list1:
#         print("".join(map(str,list1[0:len(list1)-del_num_count])))
#     else:
#         for i in range(len(list1)):
#             if i!=len(list1)-1 and list1[i] >= list1[i+1] and del_num_count > 0:
#                 del_num_count-=1
#                 dl.append(i)
#         for i in dl:
#             list1[i] = 'a'
#         list1 = list(filter(lambda x:x!='a',list1))
#         if del_num_count == 0:
#             print("".join(map(str,list1)))
#         else:
#             smalnum_aft_k_del(list1,del_num_count)

# l = list(input().split())
# n , d = list(map(int,list(l[0]))),int(l[1])
# smalnum_aft_k_del(n,d)