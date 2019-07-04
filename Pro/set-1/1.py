'''passing small len lists'''
def get_comon_prefix_len(len,list1,list2):
    common_len = 0
    for k in range(len):
        if list1[k]==list2[k]:
            common_len+=1
        else:
            break
    return common_len

i = int(input())
l,cl = [],[]
for i in range(i):
    l.append(list(input()))
# print(len(l))
for i in range(len(l)):
    if i != len(l)-1:   
        # print("i count:",i)
        list1,list2 = l[i],l[i+1]
        list1_len , list2_len = len(list1),len(list2)
        if list1_len < list2_len:
            common_len = get_comon_prefix_len(list1_len,list1,list2)
        else:
            common_len = get_comon_prefix_len(list2_len,list1,list2)
        # print("common len",common_len," for list ",list1,list2)
        cl.append(common_len)
        # print("#"*30)
print("".join(list1[:common_len]))