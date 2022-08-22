H, W = map(int,input().split()) #それぞれ別の変数

end_flag = 0
G = []
pathed_point = []
for h in range(H):
    pathed_point_list = []
    for w in range(W):
        pathed_point_list.append(0)
    pathed_point.append(pathed_point_list)

    g = input()
    G.append(g)
    if h == 0 and 'U' in g:
        end_flag = 1
    if h == H-1 and 'D' in g:
        end_flag = 1
    if g[0] == 'L':
        end_flag = 1
    if g[W-1] == 'R':
        end_flag = 1
if end_flag == 0:
    print(-1)
    exit()

i = 0
j = 0
pre_command = 'A'
while True:
    command = G[i][j]
    if pathed_point[i][j] != 0:
        print(-1)
        exit()
    pathed_point[i][j] = 1
    #print('current', i+1, j+1, '/command:', command)

    if i == 0 and command == 'U':
        print(i+1, j+1)
        exit()
    if i == H-1 and command == 'D':
        print(i+1, j+1)
        exit()
    if j == 0 and command== 'L':
        print(i+1, j+1)
        exit()
    if j == W-1 and command== 'R':
        print(i+1, j+1)
        exit()
    
    
    if command == 'U':
        i -= 1
    elif command == 'D':
        i += 1
    elif command== 'L':
        j -= 1
    elif command== 'R':
        j += 1
