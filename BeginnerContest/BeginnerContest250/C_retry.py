def swap(a,b):
    tmp = a
    a = b
    b = tmp
    return a, b

N,Q = map(int, input().split())

A = []
A_pos = []
for n in range(N):
    A.append(n+1)
    A_pos.append(n)

for q in range(Q):
    x=int(input())

    x_pos = A_pos[x-1]
    if x_pos == N-1:#右端
        y_pos = x_pos-1
    else:
        y_pos = x_pos+1
    y = A[y_pos]


    A_pos[x-1], A_pos[y-1] = swap(x_pos,y_pos)
    A[x_pos], A[y_pos] = swap(x,y)

print(*A)