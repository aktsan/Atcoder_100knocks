N = int(input())
li = [list(map(int,input().split())) for _ in range(N)]
print(li)
ans = []
for i in range(N):
    li_sum = []
    for j in range(len(li)):
        li_sum.append(li[j][0]+ (li[j][1]*i))
        print(li_sum)
    else:
        ans.append(min(li_sum))
        ind = li_sum.index(min(li_sum))
        del li[ind]
print(ans)
print(max(ans))
#解法が思い浮かばなかった