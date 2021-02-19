import math
a, b = tuple(map(int,input().split()))
# scrapped solution not efficient enough
'''
if a/2 >= b:
    c = [1]
    for i in range(int(a/2) - 1):
        c.append(c[i] + 2)
    print(c[b - 1])
else: 
    print([i*2 for i in range(1, int(a/2) + 1)][b - int(round(a/2, 0)) - 1])
'''
if math.ceil(a/2) >= b:
    print(2*(b - 1) + 1)
else:
    print(int(2*(b-(math.ceil(a/2)))))