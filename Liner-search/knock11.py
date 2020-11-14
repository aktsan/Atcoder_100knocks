from itertools import product
N,M = map(int,input().split())
ks = [list(map(int,input().split())) for _ in range(M)]
P = list(map(int,input().split()))
ans = 0
for tpl in (product([0,1], repeat = N)):
    bl = True
    for i in range(M):
        s = [tpl[j-1] for j in ks[i][1:]]
        s = sum(s)
        if (s-P[i])%2:
            bl = False
    if bl:
        ans += 1
print(ans)