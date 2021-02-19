x = int(input())
y = [input() for _ in range(x)]
for i in y:
    if len(i) > 10:
        print(i[0]+str(len(i)-2)+i[-1])
    else:
        print(i)