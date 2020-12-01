import sys
#再帰数を上げる
sys.setrecursionlimit(10**8)
ans = []
#周りを探索する関数
def dfs(x, y):
    c[x][y] = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < H and 0 <= ny < W and c[nx][ny] == 1:
                dfs(nx, ny)
while True:
    W, H = map(int, input().split())
    if W == 0 and H ==0:
        break
    count = 0
    c = [[] for _ in range(H)]
    #入力受け取り
    for i in range(H):
        if W == 1:
            c[i] = [int(input())]
        else:
            c[i] = list(map(int, input().split()))
    for x in range(H):
        for y in range(W):
            if c[x][y] == 1:
                dfs(x, y)
                count += 1
    ans.append(count)
for i in ans:
    print(i)