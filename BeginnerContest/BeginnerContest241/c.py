N = int(input())
s_list = []
for i in range(N):
    s = input()
    s_list.append(s)
    
#横のチェック
for i in range(N): #全ての行をチェックする
    this_line = s_list[i]
    if this_line.count('#') >=4:
        for j in range(N-5): #j番目の所から6つをえらんでチェックする
            this_range = this_line[j:j+6]
            sharp_num = this_range.count('#')
            if sharp_num >= 4:
                print("Yes")
                exit()


# 縦のチェック
for i in range(N):#iはチェックしたい列
    this_line =[]
    for j in range(N):
        this_line.append(s_list[j][i])
    if this_line.count('#') >=4:#そもそも4つないとあり得ない
        for j in range(N-5): #j番目の所から6つをえらんでチェックする
            this_range = this_line[j:j+6]
            sharp_num = this_range.count('#')
            if sharp_num >= 4:
                print("Yes")
                exit()


# 斜めのチェック
#(i,j)からチェックを始める
for i in range(N):
    for j in range(N):
        #右下に伸ばせるか？
        if i+6 < N and j+6 < N:
            this_line = []
            this_i = i
            this_j = j
            for count in range(6):
                this_line.append(s_list[this_j+count][this_i+count])
            if this_line.count('#') >=4:#そもそも4つないとあり得ない
                for j in range(N-5): #j番目の所から6つをえらんでチェックする
                    this_range = this_line[j:j+6]
                    sharp_num = this_range.count('#')
                    if sharp_num >= 4:
                        print("Yes")
                        exit()

        #左下に伸ばせるか？
        if i-6 > 0 and j-6 > 0:
            this_line = []
            this_i = i
            this_j = j
            for count in range(6):
                this_line.append(s_list[this_j-count][this_i-count])
            if this_line.count('#') >=4:#そもそも4つないとあり得ない
                for j in range(N-5): #j番目の所から6つをえらんでチェックする
                    this_range = this_line[j:j+6]
                    sharp_num = this_range.count('#')
                    if sharp_num >= 4:
                        print("Yes")
                        exit()            

print("No")