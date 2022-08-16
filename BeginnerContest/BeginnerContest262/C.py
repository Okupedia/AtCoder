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
a = list(map(int,input().split()))

left = 0
right = N-1
swap_count = 0
same_count = 0
while left < right:

    if left == a[left]-1:
        same_count += 1
    elif left+1 == a[a[left]-1] :
        swap_count += 1
    
    if right == a[right]-1:
        same_count += 1
    elif right+1 == a[a[right]-1]:
        swap_count += 1
    
    left += 1
    right -= 1

if left == right: #Nが奇数個のとき
    if left == a[left]-1:
        same_count += 1
    elif left+1 == a[a[left]-1] :
        swap_count += 1

ans = swap_count/2 + same_count*(same_count-1)/2
print(int(ans))