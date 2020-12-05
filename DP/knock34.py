#メモ化
N = int(input())
Memo = [0] * (N +1)
Memo[0] = 1
Memo[1] = 1
def fibonacci(N):
    for i in range(2,N+1):
        Memo[i] = Memo[i-1] + Memo[i-2]
    return Memo[N]
ans = fibonacci(N)
print(ans)