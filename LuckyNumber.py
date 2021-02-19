x = input()
ans = False 
for i in x:
    if i not in "47":
        ans = True
        break

if ans:
    x = int(x)
    if x % 4 == 0 or x % 7 == 0:
        ans = False
    else:
        for i in range(int(x/2)):
            if x % (i+1) == 0:
                ans = False
                for j in str(i+1):
                    if j not in "47":
                        ans = True
                        break

if ans is False:
    print("YES")
else:
    print("NO")


