def add_list(current_list, new_num):
    new_list = []
    for n in current_list:
        new_list.append(n+new_num)
    return new_list

bit_list = []

N = int(input())

N_bin = bin(N)
N_len = len(N_bin)

for n in range(N_len):
    i = N_len - n - 1
    if N_bin[i] == '1':
        bit_list.append(n)


ans_list = [0]

for bit in bit_list:
    new_num = 2 ** bit
    new_list = add_list(ans_list, new_num)
    for new in new_list:
        ans_list.append(new)

for ans in ans_list:
    print(ans)