N = int(input())
A1 = list(map(int,input().split()))
B1 = list(map(int,input().split()))
C1 = list(map(int,input().split()))
A1.sort()
B1.sort()
C1.sort()
#c1 > b1 > a1の通りを探索
cnt = 0
def binary_search(li,value):
    left = 0
    right = len(li) -1
    while left <= right:
        mid = (left+right) // 2
        if li[mid] == value:
            return li[:mid]
        elif li[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return li[:right+1]#value以下が入ったリストを返す
for i in range(len(C1)):
    n = binary_search(B1,C1[i])
    #print('first',n)
    for j in range(len(n)):
        m = binary_search(A1,n[j])
        #print(m)
        cnt += len(m)
print(cnt)