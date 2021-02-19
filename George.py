x = int(input())
z = [tuple(map(int,input().split())) for _ in range(x)]
i = 0
for tup in z:
    if (tup[0]+2) <= tup[1]:
        i += 1

print(i)
