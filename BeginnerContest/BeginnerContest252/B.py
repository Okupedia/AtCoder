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

N,K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

max_delicious = 0
max_delicious_index_list = []

for i in range(N):
    if A[i] > max_delicious:
        max_delicious = A[i]
        max_delicious_index_list.clear()
        max_delicious_index_list.append(i)
    elif A[i] == max_delicious:
        max_delicious_index_list.append(i)

for b in B:
    for max_delicious_index in max_delicious_index_list:
        if b-1 == max_delicious_index:
            print('Yes')
            exit()

print('No')
