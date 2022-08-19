S=input().split()
T=input().split()

flag = 0

for i in range(3):
	if S[i]==T[i]:
		flag+=1

ans = 'No'
if flag==3:#最初から全部同じ時はうまくいく
	ans = 'Yes'
#2個同じだったら３個目も同じ→flag==2はあり得ない
#1個同じの時は奇数回の交換でうまくいくからNo
elif flag==0:
	ans = 'Yes'

print(ans)
