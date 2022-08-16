def add_pre_S(S,pre_S):
    for s in pre_S:
        S.append(s)
    return S

def generate_S(N,i,S):
    pre_S=S
    S=[]
    #if i != 1:
    #    S.append(pre_S)
    S = add_pre_S(S,pre_S)
    S.append(i)
    #if i != 1:
    #    S.append(pre_S)
    S = add_pre_S(S,pre_S)
    #print('i:',i,'/pre_S:',pre_S,'/S:',S)
    if i == N:
        return S
    return generate_S(N,i+1,S)


N = int(input())
ans = generate_S(N,1,[])
print(*ans)