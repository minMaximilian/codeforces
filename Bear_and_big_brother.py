# a: original weight x 3(n)
# b: original weight x 2(n)
'''a, b = tuple(map(int,input().split()))
i = 0
while a <= b:
    i += 1
    a = a*3*i
    b = b*2*i

print(i)'''

import math

a, b = tuple(map(int,input().split()))
i = (math.log(b/a))/(math.log(3/2))
if math.ceil(i) > i: 
    print(math.ceil(i))
else:
    print(math.ceil(i) + 1) 