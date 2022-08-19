N, K, Q = map(int, input().split())

masu = [0]
for n in range(N):
	masu.append(0)

koma = list(map(int,input().split()))
for k in koma:
	masu[k] = 1

L = list(map(int,input().split()))
for l in L:
	target_masu = koma[l-1]
	if target_masu != N:
		next_masu = target_masu + 1
		if masu[next_masu] != 1:
			masu[target_masu] = 0
			masu[next_masu] = 1
			koma[l-1] = next_masu

print(*koma, sep=' ')