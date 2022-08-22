N, P, Q, R = map(int,input().split()) #それぞれ別の変数
A = list(map(int,input().split()))

sum_list = [P,Q,R]
if sum(A) < P+Q+R:
    print('No')
    exit()

pre_list = [[0,0]] #[sum, sum_list_index]
for n in range(N):
    current_num = A[n]
    current_list = [[0,0]]
    for pre in pre_list: 
        current_sum = pre[0] + current_num
        if sum_list[pre[1]]> current_sum:
            current_list.append([current_sum, pre[1]])
        elif sum_list[pre[1]] == current_sum:
            if pre[1] + 1 == 3:
                print('Yes')
                exit()
            else:
                current_list.append([0, pre[1]+1])
    pre_list = current_list

print('No')