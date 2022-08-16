#==================
#参考
#https://qiita.com/jamjamjam/items/e066b8c7bc85487c0785

### 一文字受け取る
## str型
#s = input()
## int型
#s = int(input())

### (1,N)行列を受け取る
## str型・listに格納
# s = input().split()
## str型・それぞれの変数に格納
# a, b, c = input().split()
## int型・listに格納
# s = list(map(int, input().split()))
## int型・それぞれの変数に格納
# a, b, c = map(int, input().split())
#==================

N = int(input())
range_list = []

for n in range(N):
    L_R_list = list(map(int,input().split()))
    range_list.append(L_R_list)

range_list.sort()

ans_list = []
for n in range(N-1):
    L = range_list[n][0]
    R = range_list[n][1]
    next_L = range_list[n+1][0]
    next_R = range_list[n+1][1]
    #print('[',L,',',R,') -> ','[',next_L,',',next_R,')')
    if R < next_L:
        ans_list.append([L,R])
    else:
        range_list[n+1][0] = L
        if R > next_R:
            range_list[n+1][1] = R

ans_list.append([range_list[N-1][0],range_list[N-1][1]])

for ans in ans_list:
    print(*ans, sep=' ')
