x = int(input())
y = list(map(int,input().split()))
coins = []
for i in range(x):
    if sum(y) >= sum(coins):
        coins.append(max(y))
        y.remove(max(y))

print(len(coins))