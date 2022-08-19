N, X, Y, Z = map(int,input().split())

A = list(map(int,input().split())) 
B = list(map(int,input().split())) 

math_score = []
eng_score = []
sum_score = []

passed_num_list = []

for n in range(N):
    passed_num_list.append(0)
    a = A[n]
    b = B[n]
    a_and_b = a+b
    math_score.append([a, n])
    eng_score.append([b, n])
    sum_score.append([a_and_b, n])

math_score.sort(key=lambda x:x[0],reverse=True)
eng_score.sort(key=lambda x:x[0],reverse=True)
sum_score.sort(key=lambda x:x[0],reverse=True)

ans = []
score_index = 0
for x in range(X):
    score = math_score[score_index][0]
    index = math_score[score_index][1]
    while passed_num_list[index] == 1:
        score_index +=1
        score = math_score[score_index][0]
        index = math_score[score_index][1]
    passed_num_list[index] = 1
    ans.append(index+1)

score_index = 0
for y in range(Y):
    score = eng_score[score_index][0]
    index = eng_score[score_index][1]
    while passed_num_list[index] == 1:
        score_index +=1
        score = eng_score[score_index][0]
        index = eng_score[score_index][1]
    passed_num_list[index] = 1
    ans.append(index+1)

score_index = 0
for z in range(Z):
    score = sum_score[score_index][0]
    index = sum_score[score_index][1]
    while passed_num_list[index] == 1:
        score_index +=1
        score = sum_score[score_index][0]
        index = sum_score[score_index][1]
    passed_num_list[index] = 1
    ans.append(index+1)

ans.sort()
print(*ans, sep='\n')