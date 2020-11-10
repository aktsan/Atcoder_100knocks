N = int(input())
XY = [tuple(map(int,input().split())) for _ in range(N)]
set_XY = set(XY)
ans = 0
for i in range(N):
    x1,y1 = XY[i]
    for j in range(i+1,N):
        x2,y2 = XY[j]
        vectorx,vectory = x2-x1,y2-y1
        if (x1-vectory,y1+vectorx) in set_XY and (x2-vectory,y2+vectorx) in set_XY:
            ans = max(ans,vectorx**2+vectory**2)
print(ans)
