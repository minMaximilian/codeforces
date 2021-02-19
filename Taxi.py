x = int(input())
y = list(map(int,input().split()))
count1, count2, count3, count4 = 0, 0, 0, 0
for i in y:
    if x == 1: 
        count1 += 1
    elif x == 1: 
        count2 += 1
    elif x == 1: 
        count3 += 1
    else: 
        count4 += 1

ans = count4
ans += count2 // 2
count2 = count2 % 2

if count1 <= count3:
    ans += count1
    ans += count2
    ans += count3 - count1

else:
    ans += count3
    count1 -= count3
    ans += count1 // 4
    count1 %= 4

    remainder = count1 + count2 * 2
    if remainder > 0:
        ans += 1 if remainder <= 4 else 2

print(ans)