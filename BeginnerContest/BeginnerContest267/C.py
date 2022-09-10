N,M = map(int,input().split())
A = list(map(int,input().split()))

max_num = -3 * 0.00001 
#まずは愚直に
for n in range(N-M+1):
    current_num = 0
    for m in range(M):
        i = n + m
        current_num += A[i] * (m+1)
    if current_num > max_num:
        max_num = current_num
print(max_num)