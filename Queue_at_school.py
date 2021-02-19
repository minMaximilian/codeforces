a, b = tuple(map(int,input().split()))
c = input()
c = list(c)
for i in range(b):
    indices = [i for i in range(a) if c[i] == "B"]
    for i in indices:
        if i < a - 1:
            if c[i + 1] == "G":
                c[i], c[i+1] = c[i+1], c[i]
            else:
                continue
        else: 
            break
e = ""
print(e.join(c))