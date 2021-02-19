x = int(input())
if x > 5:
    if x % 5 == 0:
        print(int(x/5))
    else:
        z = x % 5
        p = int(((x - z)/5) + 1)
        print(p)
else:
    print(1)