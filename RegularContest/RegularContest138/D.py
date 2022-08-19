N,M=map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))

B = []
reminder = [C[N+M]]
for i in range(M+1):#M+1桁の答えが出るはず
    ans = reminder[0]/A[N] #今見ている一番上の桁の計算結果
    #print('ans is ', ans)
    B.append(ans)
    reminder=[]
    for j in range(N+1):#ひっ算の一つの段ではN+1桁を計算する
        this_remind = C[N+M-i-j]-(A[N-j]*ans)
        #print('j',j,'C[N+M-i-j]',C[N+M-i-j],'/A[N-j]*ans',(A[N-j]*ans),'/this_remind',this_remind)
        C[N+M-i-j] = this_remind
        if j!=0: 
            reminder.append(this_remind)
    #print('reminder : ', reminder)    

for i in range(len(B)-1, -1, -1):
    print(int(B[i]), end = ' ')