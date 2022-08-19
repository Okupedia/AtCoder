N = int(input())
S = input()
W = list(map(int, input().split()))

weight_person_list = [] #[体重, 大人か子供か]のリストを格納するリスト
for n in range(N):
	pair = [W[n], int(S[n])]
	weight_person_list.append(pair)

best_count = -1
weight_person_list.sort(key=lambda x: x[1], reverse=True)
weight_person_list.sort(key=lambda x: x[0])

children_end_flag = 0
count = 0
for n in range(N):
	pair = weight_person_list[n]
	adult_flag = pair[1]
	weight = pair[0]
	if n == 0:
		if adult_flag == 0:
			count += 1
	else:
		if children_end_flag == 0:
			#子供が続くか大人に切り替わるかのどちらか
			if adult_flag == 0:
				#子供が続いた
				count += 1
			elif weight_person_list[n-1][1] == 0 and weight_person_list[n-1][0] != weight:
				#大人に切り替わった
				count += 1
				children_end_flag = 1
		else:#大人が来ることを期待
			if adult_flag == 1:
				count += 1
			else:#大人が来ると思ってたのに子供がきた
				if count > best_count:
					best_count == count
				count = 1#一人目から数え直す
				children_end_flag = 0
if count > best_count:
	best_count = count

print(best_count)
