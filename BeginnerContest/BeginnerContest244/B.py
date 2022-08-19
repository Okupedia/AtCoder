
N=int(input())
T=input()

x=0
y=0
direction = 0#0→東/1→南/2→西/3→北　

for i in range(N):
	if T[i]=='S':
		if direction==0:
			x+=1
		if direction==1:
			y-=1
		if direction==2:
			x-=1
		if direction==3:
			y+=1
	else:
		direction = (direction+1)%4

print(x, ' ', y)