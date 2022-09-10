N = int(input())
p = list(map(int,input().split()))

max_pesure_num = -1

#まずは全総当たり+不要なケースを削る
for n in range(N):#n個ずれたとき
    #print('n:', n)
    current_pesure_num = 0
    not_check_num = N

    for nn in range(N):
        i = (p[n] + nn) % N
        pre_plate = p[(nn-1)%N]
        current_plate = p[nn%N]
        next_plate = p[(nn+1)%N]
        #print('i', i, '// pre plate', pre_plate, 'current plate', current_plate, 'next plate', next_plate)

        if pre_plate == i or current_plate == i or next_plate == i:
            current_pesure_num += 1
        
        not_check_num -= 1

        if not_check_num < max_pesure_num - current_pesure_num:
            break

    if current_pesure_num > max_pesure_num:
        max_pesure_num = current_pesure_num

print(max_pesure_num)
