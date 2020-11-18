import copy
#配達の最短距離を出力
D = int(input())#環状線の長さ(0始まり)
N = int(input())#店舗の個数
M = int(input())#注文の個数
d1 = [int(input()) for _ in range(N-1)] #本店以外の店舗の位置
k1 = [int(input()) for _ in range(M)] #宅配先の位置
def make_d1(d1,D):#d1を成形する関数
    d1.insert(0,0)#本店の位置を追加
    d1.sort()
    tmp = copy.copy(d1)
    for i in range(len(tmp)):
        tmp[i] += D
    final_d1 = d1 + tmp
    return final_d1
d1 = make_d1(d1,D)
#絶対値で二分探索
def binary_search(li,value):
    left = 0
    right = len(li) -1
    while left <= right:
        mid = (left+right) // 2
        if li[mid] == value:
            return 0
        elif li[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return min(abs(li[right+1]-value),abs(li[left-1]-value))
cnt = 0
for i in range(len(k1)):
    n = binary_search(d1,k1[i])
    cnt += n
print(cnt)