M = int(input())
search_star = [tuple(map(int,input().split())) for _ in range(M)]
N = int(input())
pic_star = [tuple(map(int,input().split())) for _ in range(N)]
ans = []
for i in range(N):
    for j in range(M):
        tmp = (pic_star[i][0]-search_star[j][0],pic_star[i][1]-search_star[j][1])
        ans.append(tmp)
for i in range(len(ans)):
    s = ans.count(ans[i])
    if s == M:
        print(ans[i][0],ans[i][1])
        exit()