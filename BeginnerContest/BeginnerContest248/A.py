S=list(input())
num_list=list((int(i) for i in list(S)))
num_list.sort()

for i in range(9):
    if i != num_list[i]:
        print(i)
        exit()
print(9)