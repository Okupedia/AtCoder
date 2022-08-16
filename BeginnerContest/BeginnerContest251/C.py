N = int(input())

S_list = []
best_T_index = [0,0]

for n in range(N):
    s,t = input().split()
    if s not in S_list:#オリジナルのとき ←ここがボトルネック
        S_list.append(s)
        if int(t) > best_T_index[0]:#ベストスコアが更新されたとき
            best_T_index[0] = int(t)
            best_T_index[1] = n+1

print(best_T_index[1])