#countを使わずに二分探索で解く
N = int(input())
S = list(map(int,input().split()))
Q = int(input())
T = list(map(int,input().split()))
cnt = 0

def binary_search(li,value):
    left = 0
    right = len(li) -1
    while left <= right:
        mid = (left+right) // 2
        if li[mid] == value:
            return 1
        elif li[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for i in range(Q):
    if binary_search(S,T[i]):
        cnt += 1
print(cnt)