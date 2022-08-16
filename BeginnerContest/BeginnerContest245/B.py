N = int(input())
A = list(map(int,input().split()))

plus_A = [i for i in A if i >= 0]
sorted_A = sorted(list(set(plus_A)))

for i in range(len(sorted_A)):

    if i!=sorted_A[i]:
        if i != 0:
            print(sorted_A[i-1]+1)
            exit()
        else:
            print(0)
            exit()
print(len(sorted_A))