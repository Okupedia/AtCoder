H_a,W_a = map(int,input().split())
A = []
for h in range(H_a):
	a = list(map(int,input().split()))
	A.append(a)

H_b,W_b = map(int,input().split())
B = []
for h in range(H_b):
	b = list(map(int,input().split()))
	B.append(b)

matched_index_list = []#[aのh, [aのw]]
for h_b in range(H_b):
	matched_index_list.append([])
	for h_a in range(H_a):
		if set(A[h_a]) >= set(B[h_b]):
			tmp_a_w_list = []
			for w_b in range(W_b):
				for w_a in range(W_a):
					if A[h_a][w_a] == B[h_b][w_b]:
						tmp_a_w_list.append(w_a)
			matched_index_list[h_b].append([h_a,tmp_a_w_list])
	if len(matched_index_list[h_b]) == 0:
		print('No')
		exit()

#print(matched_index_list)
for i in range(len(matched_index_list[0])):
	this_w_list = matched_index_list[0][i][1]
	matched_flag = 1
	for j in range(1,H_b):
		for jj in range(len(matched_index_list[j])):
			if this_w_list not in matched_index_list[j][jj]:
					matched_flag = 0
			elif matched_index_list[0][i][0] >= matched_index_list[j][jj][0]:
				matched_flag = 0
		if matched_flag == 1:
			print('Yes')
			exit()
print('No')