def get_next_list(num_list,current_list):
	next_list = []
	for current_num in current_list:
		for next_num in num_list[current_num]:
			if next_num != 0:
				next_list.append(next_num)
	return next_list

N,M,K,S,T,X=map(int,input().split())

num_list = [[0] * 2 for i in range(N+1)]

for _ in range(M):
	U,V=map(int,input().split())
	num_list[U].append(V)
	num_list[V].append(U)

current_left = [S]
current_right = [T]

for i in range(int(K/2)):
	#print('left : ', current_left)
	next_left = get_next_list(num_list,current_left)
	current_left=next_left

	#print('right : ', current_right)
	next_right = get_next_list(num_list,current_right)
	current_right=next_right

count = 0
if K%2==0:
	#print('left : ', next_left)
	#print('right : ', next_right)
	#これ多分かなり遅い→重複なしにして出現回数分をかけたものをcountに加算する
	#for num in next_left:
	#	if next_right.count(num)!=0:
	#		count+=1
	set_left_list = list(set(next_left))
	set_right_list = list(set(next_right))
	for num in set_left_list:
		num_count = next_left.count(num)
		if set_right_list.count(num)!=0:
			print('add num is ', num, '/num_count is ', num_count)
			count+=num_count
else:
	count=0

print(int(count%998244353))
