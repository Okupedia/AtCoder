N=int(input())
s=[]
t=[]
connected_list = []
for i in range(N):
    S,T=input().split()
    s.append(S)
    t.append(T)
    if S == T:
        connected_list.append(S)
    else:
        connected_list.append(S)
        connected_list.append(T)


dup_list = [x for x in set(connected_list) if connected_list.count(x) > 1] 

for i in range(N):
    first_name = s[i]
    last_name = t[i]
    for S in dup_list:
        if first_name==S:
            for T in dup_list:
                if last_name==T:
                    print('No')
                    exit()

print('Yes')