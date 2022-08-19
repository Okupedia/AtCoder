S = input()
T = input()

S_list = []
pre_char = 'start'
current_char_count = 0

for s in S:
	if s == pre_char:
		current_char_count += 1
	else:
		char_count_pair = [pre_char, current_char_count]
		S_list.append(char_count_pair)
		pre_char = s
		current_char_count = 1

char_count_pair = [pre_char, current_char_count]
S_list.append(char_count_pair)
	
T_list = []
pre_char = 'start'
current_char_count = 0

for t in T:
	if t == pre_char:
		current_char_count += 1
	else:
		char_count_pair = [pre_char, current_char_count]
		T_list.append(char_count_pair)
		pre_char = t
		current_char_count = 1

char_count_pair = [pre_char, current_char_count]
T_list.append(char_count_pair)
	
if len(S_list) == len(T_list):
	for i in range(len(S_list)):
		current_S_char = S_list[i][0]
		current_S_char_count = S_list[i][1]
		current_T_char = T_list[i][0]
		current_T_char_count = T_list[i][1]


		if current_S_char == current_T_char:
			if current_S_char_count != current_T_char_count:
				if current_T_char_count < current_S_char_count:
					print('No')
					exit()
				elif current_S_char_count < 2:
					print('No')
					exit()
		else:
			print('No')
			exit()
	print('Yes')
else:
	print('No')
