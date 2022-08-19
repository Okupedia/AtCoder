N,K=map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

current_pair = [A[0],B[0]]
for i in range(N-1):
    next_possible_pair = [A[i+1],B[i+1]]
    next_pair = []

    for this_num in current_pair:
        for next_num in next_possible_pair:
            if abs(this_num-next_num)<=K:
                next_pair.append(next_num)

    current_pair = list(set(next_pair))

    if len(current_pair)==0:
        print('No')
        exit()

if len(current_pair)==0:
    print('No')
else:
    print('Yes')