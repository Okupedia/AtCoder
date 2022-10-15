N = int(input()) 
a = list(map(int,input().split()))

current_num = 0
current_pointer = 0
end_pointer = N-1

for n in range(N):
    if N < 3 and a[0] != 1:
        break
    current_num += 1
    if a[current_pointer] == current_num:
        current_pointer += 1
    elif a[current_pointer] != current_num:
        end_pointer -= 2
    #print('num:', current_num,'pointer:', current_pointer, '->', end_pointer)
    if current_pointer == end_pointer:
        #print('a[current_pointer]', a[current_pointer])
        if a[current_pointer] == current_num + 1:
            current_num += 1
        break
    elif current_pointer > end_pointer:
        break

print(current_num)