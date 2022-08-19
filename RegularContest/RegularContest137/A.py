def is_prime(q):#フェルマーの小定理
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def check_gcd(x, y, L, R, prime_flag):
	if prime_flag == 1:#xが素数だとわかっている
		#最小がL~xの中で、差分がR-x以内でありがながら互いに素な値がないかを調べる
		for diff in range(R-L, R-x, -1):
			for min in range(L,x):
				max = min + diff
				#print('min:',min, ' max:',max)
				if max <= R:
					if gcd(min, max)==1:
						print(diff)
						exit()
		print(R-x)
		exit()
	if prime_flag == 2:#yが素数だとわかっている
		#最大がy~Rの中で、差分がy-L以内でありがながら互いに素な値がないかを調べる
		for diff in range(R-L, y-L, -1):
			for max in range(R,y, -1):
				min = max - diff
				#print('min:',min, ' max:',max)
				if min >= L:
					if gcd(min, max)==1:
						print(diff)
						exit()
		print(y-L)
		exit()
	return

L,R=map(int,input().split())

if L == 1:
	print(R-L)
	exit()

for i in range(R-L):
	x = L+i
	if is_prime(x):
		#print(x, 'is prime')
		if gcd(x,R)==1:
			check_gcd(x, y, L, R, 1)
	y = R-i
	if is_prime(y):
		#print(y, 'is prime')
		if gcd(L,y)==1:
			check_gcd(x, y, L, R, 2)
print(1)#連続値は必ず互いに素