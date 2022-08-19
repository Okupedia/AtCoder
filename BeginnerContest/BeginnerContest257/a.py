N, X = map(int,input().split())

count = 0
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for word in alphabet:
	for n in range(N):
		count += 1
		if count == X:
			print(word)
