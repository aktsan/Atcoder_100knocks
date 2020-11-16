from itertools import combinations
N, M = map(int, input().split())
relations = [[0 for i in range(N)] for _ in range(N)]
#N番目の人は誰と仲いいかを記録
for m in range(M):
    x, y = map(int, input().split())
    relations[x-1][y-1] = 1 #indexなので一つずらして記録\:
    relations[y-1][x-1] = 1
#print(relations)
for i in range(N,1,-1): # N, N-1, N-2
    for comb in combinations(range(N),i):
        #print("#########")
        #print(comb)
        for c in combinations(comb, 2): # 議員の集合に対して考えられるペアを列挙
            #print(c)
            if (relations[c[0]][c[1]] == 0): # 一つでも知り合いでない組があればNG
                break
        else: # 派閥が作れた段階でプログラムを終了
            print (i)
            exit()
print (1)