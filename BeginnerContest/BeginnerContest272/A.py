N, Q = map(int,input().split())

L_list = []
for n in range(N):
    l = list(map(int,input().split()))
    L_list.append(l)

s_t_list = []
for q in range(Q):
    s, t = map(int,input().split())
    s_t_list.append([s,t])
    
for q in range(Q):
    s = s_t_list[q][0]
    t = s_t_list[q][1]
    print(L_list[s-1][t])
