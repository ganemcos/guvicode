import collections as c
null = input()
i = map(int,input().split())
ocr = c.Counter(i)
for item,count in ocr.items():
    if count >1 :
        print(item,end= " ")