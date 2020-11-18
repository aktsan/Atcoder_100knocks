from itertools import permutations 
n = int(input())
P = tuple(map(int,input().split()))
Q = tuple(map(int,input().split()))
li = list(permutations(range(1,n+1)))
p_index = 0
q_index = 0
for i in range(len(li)):
    if li[i] == P and li[i] == Q:
        print(0)
        exit()
    if li[i] == P:
        p_index = i+1
    elif li[i] == Q:
        q_index = i+1
print(abs(p_index-q_index))

#これは意外と簡単やった