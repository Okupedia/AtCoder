N = int(input())
A = list(map(int,input().split()))

A = sorted(A)
#ダメなケースの列挙
if N == 2:
    if A[0] == 0:
        if A[1]%2 != 0:
            print(-1)
            exit()
    if A[0]%2 != 0:
        if A[1]%2 == 0:
            print(-1)
            exit()
    if A[0]%2 == 0:
        if A[1]%2 != 0:
            print(-1)
            exit()

if N == 3:
    if A[0] == 0:
        if A[1]%2 != 0:
            if A[2]%2 == 0:
                print(-1)
                exit()
        if A[1]%2 == 0:
            if A[2]%2 != 0:
                print(-1)
                exit()

if A[N-1]%2 == A[N-2]%2:
    print(A[N-1]+A[N-2])
    exit()
if A[N-1]%2 == A[N-3]%2:
    print(A[N-1]+A[N-3])
    exit()

max_num_odd_flag = A[N-1]%2
current_max_sum = A[N-2] + A[N-3]
current_sum = -1
for n in range(4,N+1):
    current_num = A[N-n]
    if current_num%2 == max_num_odd_flag:
        current_sum = A[N-1] + current_num
        break

if current_sum > current_max_sum:
    print(current_sum)
else:
    print(current_max_sum)
