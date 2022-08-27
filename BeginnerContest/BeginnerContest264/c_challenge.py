def check(A, H_a, W_a, B, H_b, W_b, h_bit, w_bit):
	B_h_index = 0
	B_w_index = 0

	#チェックをする
	for current_h in range(H_a):
		if (1 << current_h) & h_bit == 0:
			#消していない行について
			for current_w in range(W_a):
				if (1 << current_w) & w_bit == 0:
					#このマスは消していないはず
					if B_h_index < H_b:
						a = A[current_h][current_w]
						b = B[B_h_index][B_w_index]
						if a != b:
							return 0
						else:
							B_w_index += 1
							if B_w_index == W_b:
								B_w_index = 0
								B_h_index += 1
					else:
						return 0
	if B_h_index == H_b and B_w_index == 0:
		return 1
	else:
		return 0

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

#bit全探索をする
for bit in range(1<<(H_a+W_a)):
	#今回試すパターン
	w_bit = bit & ( (2 ** W_a) - 1)
	h_bit = bit >> W_a
	yes_flag = check(A, H_a, W_a, B, H_b, W_b, h_bit, w_bit)
	if yes_flag == 1:
		print('Yes')
		exit()

print('No')