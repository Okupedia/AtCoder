N,M,K=map(int,input().split())

current_list=[]
for m in range(M):
    current_list.append(1)
#next_list_default = []
#for k in range(K):
#    next_list_default.append(0)

for n in range(N-1):#最初にやっているから試行回数はN-1回
    next_list=[]
    for k in range(K):
        next_list.append(0)

    for current_index in range(len(current_list)):#今の状態:current_index+1
        current_num = current_list[current_index]
        for m in range(M):#次の数字候補:m+1
            next_sum = (m+1)+(current_index+1)
            if next_sum <= K:
                #print('current_index+1:',current_index+1,'m+1:',m+1,'next_sum:',next_sum)
                next_list[next_sum-1]+=current_num
    #print('current_list:',current_list)
    #print('   next_list:',next_list)
    #print('========================')
    current_list=next_list

sum = 0
for num in current_list:
    sum += num
print(sum%998244353)