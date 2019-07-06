import string
c =0 
l = list(input())
# print(set(string.punctuation))
for i in l:
    if i in set(string.punctuation):
        c+=1
print(c)