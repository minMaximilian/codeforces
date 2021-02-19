x = input()
target = "hello"
ans = []
for i in x:
    if i not in target:
        continue
    else:
        ans.append(i)
ans_2 = []
for i in ans:
    if i == "h" and "h" not in ans_2:
        ans_2.append("h")
    elif i == "e" and "e" not in ans_2:
        ans_2.append("e")
    elif i == "l" and ans_2.count("l") != 2:
        ans_2.append("l")
    elif i == "o" and "o" not in ans_2:
        ans_2.append("o")
    elif len(ans) == 5:
        break
for i in target:
    if i != "l" and ans.count(i) > 1:
        while ans.count(i) != 1:
            ans.remove(i)
    elif i == "l":
        while ans.count("l") != 2:
            ans.remove("l")
    else:
        break

ans = "".join(ans)
ans_2 = "".join(ans_2)
if ans == target or ans_2 == target:
    print("YES")
else:
    print("NO")