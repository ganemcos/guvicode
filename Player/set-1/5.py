s = list(input())
romdata = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
num =0
for i in range(len(s)):
    if i>0 and (romdata[s[i]] > romdata[s[i-1]]):
        num += romdata[s[i]] -2 *romdata[s[i-1]]
    else:
        num +=romdata[s[i]]

print(num)