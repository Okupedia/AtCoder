import itertools

N,W = map(int,input().split())
A = list(map(int,input().split()))

combinations_list = []
count = 0
sum_list = []

for i in range(1,4):
    combination = list(itertools.combinations(A, i))
    for comb in combination:
        current_sum = 0
        for num in comb:
            current_sum += num
            if current_sum > W:
                break
        if current_sum <= W:
            #print('current_sum:',current_sum)
            sum_list.append(current_sum)
            if len(sum_list) != len(set(sum_list)):
                sum_list = list(set(sum_list))
            else:
                count += 1

print(count)