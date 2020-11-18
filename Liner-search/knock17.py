from itertools import permutations
K = int(input())
ex_queens = [tuple(map(int,input().split())) for _ in range(K)]
print(ex_queens)
board = [list('.'*8) for _ in range(8)]
print(board)
li = list(permutations(range(8))  )
#print(li)
#わからんから飛ばしました