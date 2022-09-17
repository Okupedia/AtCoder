def all_down_check(s,a,b):
    a -= 1
    b -= 1
    if s[a] == '0' and S[b] == '0':
        return 1
    return 0

S = input()

if S[0] == '1':
    print('No')
    exit()

line_all_down_flag = [0,0,0,0,0,0,0]

line_all_down_flag[0] = all_down_check(S,1,7)
line_all_down_flag[1] = all_down_check(S,1,4)
line_all_down_flag[2] = all_down_check(S,2,8)
line_all_down_flag[3] = all_down_check(S,1,5)
line_all_down_flag[4] = all_down_check(S,3,9)
line_all_down_flag[5] = all_down_check(S,1,6)
line_all_down_flag[6] = all_down_check(S,1,10)

left_stand_index = -1
right_stand_index = -1

current_index = 0
while left_stand_index == -1:
    if line_all_down_flag[current_index] == 0:
        left_stand_index = current_index
    current_index += 1
    if current_index == 7:
        print('No')
        exit()

current_index = 6
while right_stand_index == -1:
    if line_all_down_flag[current_index] == 0:
        right_stand_index = current_index
    current_index -= 1
    if current_index == left_stand_index:
        print('No')
        exit()

for i in range(left_stand_index+1,right_stand_index):
    if line_all_down_flag[i] == 1:
        print('Yes')
        exit()

print('No')