x = input()
check_h = False
check_e = False
check_l = False
check_ll = False
check_o = False
for i in x: 
    if i == "h":
        check_h = True
    elif i == "e" and check_h:
        check_e = True
    elif i == "l" and check_e and not check_l:
        check_l = True
    elif i == "l" and check_l:
        check_ll = True
    elif i == "o" and check_ll:
        check_o = True

if check_h and check_e and check_l and check_ll and check_o:
    print("YES")
else:
    print("NO")