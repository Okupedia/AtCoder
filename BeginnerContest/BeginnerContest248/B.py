def shout(A,B,K,count):
    if A >= B:
        return count
    A = A*K
    return shout(A,B,K,(count+1))

A,B,K=map(int,input().split())
ans = shout(A,B,K,0)
print(ans)