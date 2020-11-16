A,B,C,X,Y = map(int,input().split())
ans = 0
if A+B <= C*2:
    ans = A*X + B*Y
else:
    if X >= Y:
        ans  = min(A*(X-Y) + C*2*Y,C*2*X)
    else:
        ans = min(B*(Y-X) + C*2*X, C*2*Y)
print(ans)