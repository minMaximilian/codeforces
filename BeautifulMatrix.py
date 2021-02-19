matrix = [tuple(map(int,input().split())) for _ in range(5)]
for i in matrix:
    if 1 in i:
        x = i.index(1)
        y = matrix.index(i)
        break
print((abs(2 - x) + abs(2 - y)))

