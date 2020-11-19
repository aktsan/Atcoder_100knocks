N = int(input())
A1 = list(map(int,input().split()))
B1 = list(map(int,input().split()))
C1 = list(map(int,input().split()))
A1.sort()
B1.sort
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
    return li[:right+1]

def binary_search2(li,value):
    left = 0
    right = len(li) -1
    while left <= right:
        mid = (left+right) // 2
        if li[mid] == value:
            return li[mid+1:]
        elif li[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return li[right+1:]
#解説に沿った解答にしたつもりやけどTLE
#TLE24で増えてるんですけど
for i in range(len(B1)):
    n = binary_search(A1,B1[i])
    m = binary_search2(C1,B1[i])
    print('key:',B1[i],n,m)
    cnt += len(n)*len(m)
print(cnt)  
#最初に作った解答やけどTLE(22個) 
#value以下が入ったリストを返す
#for i in range(len(C1)):
#    print('key:',C1[i])
#    n = binary_search(B1,C1[i])
#    print('first',n)
#   for j in range(len(n)):
#        m = binary_search(A1,n[j])
#        print(m)
#       cnt += len(m)
#print(cnt)