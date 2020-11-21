import bisect
N, M, *P = [int(_) for _ in open(0).read().split()]
dp = [set() for _ in range(3)]
dp[0].add(0)
for p in P:
    for i in range(2):
        for x in dp[i]:
            if x + p <= M:
                dp[i + 1].add(x + p)
li = sorted(dp[0] | dp[1] | dp[2])
ans = max(x + li[min(len(li), bisect.bisect_right(li, M - x)) - 1] for x in li)
print(ans)