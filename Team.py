x = int(input())
y = [tuple(map(int,input().split())) for _ in range(x)]
m = 0 
for i in y:
    l = 0
    for j in i:
        if j == 1:
            l += 1
            if l >= 2:
                m += 1
                break

print(m)
