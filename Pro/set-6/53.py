import string
alphabet = set(string.ascii_lowercase)
l = list(input().replace(" ",""))
l = set([l[i].lower() for i in range(len(l))])
# print(l,alphabet,sep = "\n")
print("yes" if set(l) == set(alphabet) else "no")