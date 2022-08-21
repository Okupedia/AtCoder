N,M,T = map(int,input().split()) #それぞれ別の変数

A = list(map(int,input().split())) #複数の整数(リスト)

index_A = 0
need_time = 0
for m in range(M):
    x,y = map(int,input().split()) #それぞれ別の変数
    for i in range(index_A,x-1):
        #print('i:', i)
        need_time += A[i]
    index_A = x-1
    #print('T:', T, 'need_time:', need_time)
    if need_time >= T:
        print('No')
        exit()
    else:
        T -= need_time
        T += y
    need_time = 0
if index_A < N:
    for i in range(index_A,N-1):
        #print('i:', i)
        need_time += A[i]
    #print('T:', T, 'need_time:', need_time)
    if need_time >= T:
        print('No')
        exit()
print('Yes')