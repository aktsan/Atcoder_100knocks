N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
 
ans = 10**13
for i in range(N):
    #入口
    X = li[i][0]
    for j in range(N):
        #出口
        Y = li[j][1]
        total = 0
        for k in range(N):
            #座標
            A,B= li[k][0], li[k][1]
            total += abs(B-A) + abs(A-X) + abs(B-Y)
        ans = min(ans,total)
print(ans)