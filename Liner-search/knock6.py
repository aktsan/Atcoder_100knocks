N = int(input())
S = input()
cnt = 0
for i in range(10):
    a = S.find(str(i))
    for j in range(10):
        b = S.find(str(j),a+1)
        for k in range(10):
            c = S.find(str(k),b+1)
            if a != -1 and b != -1 and c != -1:
                cnt += 1
print(cnt)