N = int(input())
A_s = list(map(int,input().split()))
Q = int(input())
li = list(map(int,input().split()))
A_sums = []
for i in range(2**N):
    sums = 0
    for j in range(N):
        if ((i >> j) & 1):
            sums += A_s[j]
    A_sums.append(sums)

for i in range(Q):
    if li[i] in A_sums:
        print('yes')
    else:
        print('no')