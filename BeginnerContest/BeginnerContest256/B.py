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
#a, b, c = map(int, input().split())
#==================

N = int(input())
A = list(map(int,input().split()))
count = 0
trout = []
trout_start = 0
trout_count = 0

for n in range(N):
    trout.append(0)
    trout_count += 1
    for i in range(trout_start,trout_count):
        trout[i] += A[n]
        if trout[i] > 3:
            count += 1
            trout_start += 1

print(count)