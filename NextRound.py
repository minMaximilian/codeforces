output=tuple(map(int,input().split()))
scores=tuple(map(int,input().split()))
m, n = output
j = 0
for i in scores:
    if i < scores[n-1] or i == 0:
        break
    j += 1

print(j)