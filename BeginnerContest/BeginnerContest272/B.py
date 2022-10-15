N, M = map(int, input().split())

connected_num = []
connected_flag = []

for n in range(N):
    connected_num.append(0)
    connected_flag_list = []
    for nn in range(n,N-1):
        connected_flag_list.append(0)
    connected_flag.append(connected_flag_list)


for m in range(M):
    this_list = list(map(int, input().split()))
    K = this_list[0]

    for k in range(1, K):
        x = this_list[k]
        for kk in range(k+1, K+1):
            xx = this_list[kk]
            if connected_flag[x-1][xx-(x+1)] == 0:
                connected_flag[x-1][xx-(x+1)] = 1
                connected_num[x-1] += 1

for n in range(N):
    this_num = connected_num[n]
    if this_num != N-(n+1):
        print('No')
        exit()
print('Yes')
