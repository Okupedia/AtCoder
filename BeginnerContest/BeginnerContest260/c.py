N, X, Y = map(int,input().split())

current_red = 1
current_blue = 0
for n in range(N-1):
	created_blue = current_red * X
	next_red = current_red + created_blue + current_blue
	next_blue = (current_blue + created_blue) * Y
	current_red = next_red
	current_blue = next_blue
	#print('count:', n, '/red:', current_red, '/blue:', current_blue)

print(current_blue)