x = int(input())
y = input()
z = 0
i = 0
while i != x-1:
    if y[i] == y[i+1]:
        z += 1
    i += 1

print(z)
