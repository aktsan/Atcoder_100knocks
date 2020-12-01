N = int(input())
#頂点番号と揃える
li = [[0,0,0]]+[list(map(int,input().split())) for _ in range(N)]
stack = []
visited = []
time = 0
d = [0] * (N + 1) #発見時刻のリスト
f = [0] * (N + 1) #完了時刻のリスト
for i in range(1, N + 1):
    if i not in visited:
        stack.append(i)
        visited.append(i)
        time += 1
        d[i] = time

        while stack: #stackに数字が入っている限り
            s = stack[-1] #探索する頂点
            k = li[s][1] #その頂点に隣接する頂点の数
            #print('s:',s)
            #print('k:',k)
            #print('####')
            if k == 0: #何も隣接していなかったら時間を入れて終了
                stack.pop() #末尾を消去
                time += 1
                f[s] = time
            else:
                li[s][1] -= 1 #探索済みの分数を減らす
                v = li[s].pop(2) #隣接する頂点が一番小さい頂点
                #print('v:',v)
                if v not in visited:
                    stack.append(v)
                    visited.append(v)
                    time += 1
                    d[v] = time

for i in range(1, N + 1):
    print(i, d[i], f[i])