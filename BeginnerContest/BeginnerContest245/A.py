A,B,C,D=map(int,input().split())

T = 'Takahashi'
Ao = 'Aoki'
if A > C:
    ans = Ao
elif C > A:
    ans = T
else:
    if B>D:
        ans =Ao
    else:
        ans =T
        
print(ans)