import collections as c
null = input()
i = map(int,input().split())
ocr = c.Counter(i)
common = []
for item,count in ocr.items():
    if count >1 :
        common.append(item)
if common:
    print(*common)
else:
    print("unique")