from collections import deque

N, Q = map(int, input().split())
d = deque()

S = input()
for n in range(N):
	d.append(S[n])

for q in range(Q):
	s, x = map(int, input().split())

	if s == 1:
		for i in range(x):
			poped = d.pop()
			d.appendleft(poped)
	if s == 2:
		print(d[x-1])
