import collections as c
import operator
i = list(input())
ocr = c.Counter(i)
max_ocr_ele  =  max(ocr.items(),key = operator.itemgetter(1))[0]
print(max_ocr_ele)