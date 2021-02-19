x = int(input())
y = [tuple(map(int,input().split())) for i in range(x)]
z = 0
j = 0 
for i in y:
    z = z - i[0]
    z = z + i[1]
    if z > j:
        j = z

print(j)
