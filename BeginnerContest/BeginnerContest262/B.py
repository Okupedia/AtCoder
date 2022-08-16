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

N,M = map(int,input().split())

graph_list = []
for i in  range(N):
    graph_list.append([])

for m in range(M):
    u,v = map(int,input().split())
    graph_list[u-1].append(v-1)
    graph_list[v-1].append(u-1)

#print(graph_list)

count = 0
for i in range(len(graph_list)):
    first_num = i
    for j in range(len(graph_list[first_num])):
        second_num = graph_list[first_num][j]
        for jj in range(len(graph_list[second_num])):
            third_num = graph_list[second_num][jj]
            for jjj in range(len(graph_list[third_num])):
                if first_num == graph_list[third_num][jjj]:
                    #print(first_num, ',', second_num, ',', third_num, '//', graph_list[third_num][jjj])
                    count += 1

print(int(count/6))