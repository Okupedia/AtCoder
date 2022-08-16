S = input()

length = len(S)

repeat = int(6/length)
left = 6-length*repeat
#print('repeat:',repeat,'/left:',left)

for i in range(repeat):
    print(S,sep='',end='')
for i in range(left):
    print(S[i],end='')