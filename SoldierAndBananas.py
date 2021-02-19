k, n, w = tuple(map(int,input().split()))
j = 0
for i in range(w+1):
    j += i*k

if 0 > j-n:
    print(0)
else:
    print(j-n)
