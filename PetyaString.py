x = list(input().lower())
y = list(input().lower())
x.sort()
y.sort()
x = "".join(x)
y = "".join(y)
ans = 0
print(x)
print(y)
for i in range(len(x)):
    if x[i] > y[i]:
        ans = 1
        break
    elif x[i] < y[i]:
        ans = -1
        break
print(ans)