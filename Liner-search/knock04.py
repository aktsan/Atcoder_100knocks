N,M = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(N)]
max_sum= []
for i in range(M):
    for j in range(i+1,M):
        num_sum = []
        for k in range(N):
            X = max(li[k][i],li[k][j])
            #print(i,j,X)
            num_sum.append(X)
        max_sum.append(sum(num_sum))
print(max(max_sum))