N = int(input())

A = []
max_num = -1
mux_num_index_list = []
for n in range(N):
	a = input()
	a_list = []
	for i in range(N):
		num = int(a[i])
		a_list.append(num)
		if num > max_num:
			max_num = num
			max_num_index_list = []
			max_num_index_list.append([i, n])
		elif num == max_num:
			max_num_index_list.append([i,n])
	A.append(a_list)


#最大値を含むように考えていく
candidate_numbers_list = []
for max_num_index in max_num_index_list:
	horizontal_index = max_num_index[0]
	vertical_index = max_num_index[1]

	#縦を見る →horizontalを固定
	candidate_numbers = []
	for n in range(N):
		candidate_numbers.append(A[(vertical_index + n) % N][horizontal_index])
	candidate_numbers_list.append(candidate_numbers)

	candidate_numbers = []
	for n in range(N):
		candidate_numbers.append(A[(vertical_index - n) % N][horizontal_index])
	candidate_numbers_list.append(candidate_numbers)

	#横を見る →verticalを固定
	candidate_numbers = []
	for n in range(N):
		candidate_numbers.append(A[vertical_index][(horizontal_index + n) % N])
	candidate_numbers_list.append(candidate_numbers)

	candidate_numbers = []
	for n in range(N):
		candidate_numbers.append(A[vertical_index][(horizontal_index - n) % N])
	candidate_numbers_list.append(candidate_numbers)

	#右斜めを見る
	candidate_numbers = []
	for n in range(N):
		v = (vertical_index - n) % N
		h = (horizontal_index + n) % N
		candidate_numbers.append(A[v][h])
	candidate_numbers_list.append(candidate_numbers)

	candidate_numbers = []
	for n in range(N):
		v = (vertical_index + n) % N
		h = (horizontal_index - n) % N
		candidate_numbers.append(A[v][h])
	candidate_numbers_list.append(candidate_numbers)

	#左斜めを見る
	candidate_numbers = []
	for n in range(N):
		v = (vertical_index + n) % N
		h = (horizontal_index + n) % N
		candidate_numbers.append(A[v][h])
	candidate_numbers_list.append(candidate_numbers)

	candidate_numbers = []
	for n in range(N):
		v = (vertical_index - n) % N
		h = (horizontal_index - n) % N
		candidate_numbers.append(A[v][h])
	candidate_numbers_list.append(candidate_numbers)

candidate_numbers_list.sort(reverse=True)
print(*candidate_numbers_list[0], sep = '')