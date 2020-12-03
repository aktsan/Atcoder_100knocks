from collections import deque
N = int(input())
li = [[0,0]]+[list(map(int,input().split())) for _ in range(N)]
#print(li)
#時間を表す
vector = [[0] for i in range(N+1)]
#発見済みでまだ行ってないところ
queue = []
visited = []
time = 0
d = deque()
d.append(1)
#print(d)
while d:
    #起点を抜き出す
    v = d.popleft()
    #まだ来てなかったら時間を記録
    if vector[v] == [0]:
        vector[v] = time
    #print('v=',v)
    #print(vector)

    if v not in queue:
        #来たことを記録
        visited.append(v)
        queue.append(v)
        #何個つながってるかを記録
        k = li[v][1]
        #つながってるところを記録
        if k != 0:
            for i in range(2,2+k):
                if li[v][i] not in d:
                    d.append(li[v][i])

        
        time += 1
        for j in d:
            if j not in visited:
                vector[j] = vector[v]+1
        for i in d:
            visited.append(i)
        #print('d:',d)
        #print('vector:',vector)
        #print('queue:',queue)
        #print('time:',time)
    else:
        time -= 1
        #print(time)
for i in range(1,N+1):
    print(i,end=' ')
    if vector[i] == [0]:
        print(-1)
    else:
        print(vector[i])
