from itertools import combinations
N,K = map(int, input().split())
li = list(map(int, input().split()))
mn = 10**18
for B in combinations(range(1,N),K-1): # 一番左以外のN-1個からK-1個を選ぶ組み合わせ
    #rint(B)
    mx = li[0] # 初期値は一番左の建物
    score = 0
    for n in range(1,N):
        if n in B: # 見えるようにすべき建物なら
            if li[n] <= mx: # 低ければ高くする
                mx += 1
                score += (mx - li[n])
            else: # 高さが十分なら何もしない。最大値を更新
                mx = li[n]
        else:
            mx = max(mx, li[n]) # 見えなくても良い建物なら、最大値を更新
    mn = min(mn, score)
print (mn)