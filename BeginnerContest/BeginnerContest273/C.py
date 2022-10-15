N = int(input())
A = list(map(int,input().split()))

sorted_A = sorted(A, reverse=True)
set_A = sorted(set(sorted_A), reverse=True)
#print(sorted_A)
#print(set_A)

current_index = 0
current_ans_count = 0

while current_index < N:
    for n in(set_A):
        #print('target num is', n)
        num = sorted_A[current_index]
        #print('current num is', num)
        current_count = 0
        while num == n:
            current_count += 1
            current_index += 1
            if current_index != N:
                num = sorted_A[current_index]
            else:
                num = -1
        print(current_count)
        current_ans_count += 1

while current_ans_count < N:
    print(0)
    current_ans_count += 1
