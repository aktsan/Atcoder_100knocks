from collections import deque
R,C = map(int,input().split())
sy,sx = map(int,input().split())
gy,gx = map(int,input().split())
#indexを揃えるため
stage = [['nemui']]+[[['a']]+list(input()) for _ in range(R)]
#時間を表す
time = 0
#探索済み
visited = []
#時間を記録する
vector = [[0] * (C+1) for _ in range(R+1)]
#探索方向
dir = [[0,1],[0,-1],[1,0],[-1,0]]
d = deque()
d.append([sy,sx])
vector[sy][sx] = time
cnt = 0
while d:
    #探索点の取り出し
    v = d.popleft()
    #print('v:',v)
    if v not in visited:
        visited.append(v)
    #時間を記録
    #if vector[v[1]][v[0]] != 0:
    #    vector[v[1]][v[0]] = time
    #    time += 1
    #print('visited:',visited)
    for i in dir:
        #print(i)
        if v[1]+i[1] > R or v[0]+i[0] > C:
            pass
        else:
            if stage[v[0]+i[0]][v[1]+i[1]] == '.':
                #もう探索済みの物は追加しない

                if [v[0]+i[0],v[1]+i[1]] not in visited:
                    if v[0]+i[0] == gy and v[1]+i[1] == gx:
                        #print('Yes')
                        print(vector[v[0]][v[1]] + 1)
                        exit()
                    #print('nemui',v[0]+i[0],v[1]+i[1])   
                    d.append([v[0]+i[0],v[1]+i[1]])
    
    for i in d:
        #print('i',i)
        if i not in visited:
            #print(i)
            vector[i[0]][i[1]] = vector[v[0]][v[1]] + 1
            visited.append(i)
    #print('after added d:',d)
    #print(vector)
    #print('############')
    cnt += 1
    #if v[1] == gy and v[0] == gx:
    #    print('Yes')
    #    exit()
    #if cnt == 19:
    #   exit()

        
