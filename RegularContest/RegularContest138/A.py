N,K=map(int,input().split())
A=list(map(int,input().split()))

biggest_A = sorted(A,reverse=True)

sum = 0
biggest_sum= 0

small_A = A[0]
small_A_index = 0


for i in range(K):
    sum += A[i]
    biggest_sum += biggest_A[i]
    if A[i] <= small_A:
        small_A = A[i]
        small_A_index = i

#print('sum:',sum,'/biggest_sum:',biggest_sum)

if biggest_sum <= sum:
    print(-1)
    exit()

big_A_index=0
big_A=0
for i in range(K,N):
    big_A = A[i]
    if A[i] > small_A:
        big_A_index = i
        break
#print('small_A:',small_A,'/small_A_index:',small_A_index,'//big_A:',big_A,'/big_A_index:',big_A_index)
#min_diff = (K-small_A_index)+(big_A_index-K)
min_diff = big_A_index-small_A_index

for small_index in range(small_A_index+1,K):
    for max_index in range(K, big_A_index+1):
        if A[small_index] < A[max_index]:
            if min_diff > max_index-small_index:
                min_diff = max_index-small_index

print(min_diff)