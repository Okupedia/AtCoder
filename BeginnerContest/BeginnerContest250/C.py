def print_list(right_list,N):
    next_index = right_list[0]
    for n in range(N):
        print(next_index, end=' ')
        next_index = right_list[next_index]
    return

N,Q = map(int, input().split())

right_list = []
left_list = []
right_list.append(1)
left_list.append(N)
for n in range(N):
    if n == 0:
        right_list.append(n+2)
        left_list.append(N)
    elif n != N-1:
        right_list.append(n+2)
        left_list.append(n)
    else:
        right_list.append(1)
        left_list.append(n)

for q in range(Q):
    x = int(input())
    w = left_list[x]
    y = right_list[x]
    z = right_list[y]
    if x != N:
        right_list[w] = y
        right_list[y] = x
        left_list[y] = w
        right_list[x] = z
        left_list[x] = y
        left_list[z] = x
    else:
        w_left = left_list[w]
        right_list[w_left] = x
        left_list[y] = w
        left_list[x] = w_left
        right_list[x] = w
        left_list[w] = x
        right_list[w] = y

    if x == right_list[0]:
        right_list[0] = y
    

print_list(right_list,N)