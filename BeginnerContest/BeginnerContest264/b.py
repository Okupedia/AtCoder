R,C = map(int,input().split())

if R > 8:
    R = 16 - R
if C > 8:
    C = 16 - C

black_list = [1,3,5,7]

large_num = C
small_num = R
if R >= C:
    large_num = R
    small_num = C

if small_num in black_list:
    print('black')
else:
    print('white')

