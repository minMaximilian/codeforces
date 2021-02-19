output=tuple(map(int,input().split()))
n, m, a = output
import math
ans = (math.ceil(n/a)) * (math.ceil(m/a))
print(ans)
