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
def check_row(h_list,w):
    ans = []
    for i_00 in range(h_list[0]+1):
        for i_01 in range(h_list[1]+1):
            for i_02 in range(h_list[2]+1):
                if w-i_00-i_01-i_02 == 0:
                    ans.append([i_00, i_01, i_02])
    return ans


sum_list = list(map(int,input().split()))

h = [sum_list[0]-3, sum_list[1]-3, sum_list[2]-3]
w = [sum_list[3]-3, sum_list[4]-3, sum_list[5]-3]

if sum(h) != sum(w):
    print(0)

#4つ見れば決まるのだから総当たりでよくない？
