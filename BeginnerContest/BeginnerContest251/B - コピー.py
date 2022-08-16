N,W = map(int,input().split())
A = list(map(int,input().split()))

W_list = []

for w in range(W):
    W_list.append(0)

#1つを選ぶよ
for i in range(N):
    sum = A[i]
    if sum <= W:
        W_list[sum-1] = 1

#2つを選ぶよ
for i in range(N):
    for ii in range(i+1,N):
        sum = A[i] + A[ii]
        if sum <= W:
            W_list[sum-1] = 1

#3つを選ぶよ
for i in range(N):
    sum = 0
    for ii in range(i+1,N):
        for iii in range(ii+1,N):
            sum = A[i] + A[ii] + A[iii]
            if sum <= W:
                W_list[sum-1] = 1

print(W_list.count(1))