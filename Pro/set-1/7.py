import math
i = int(input())
res = int(math.pow( 2, round( math.log( i ) / math.log( 2 ) ) ))
if res == i:
    print(0)
else:
    print(i-res)
