a_flag = 0
c_flag = 0

A = -1
B = -1
C = -1
D = -1

for n in range(10):
    s = input()
    if '#' in s and a_flag == 0:
        A = n
        a_flag = 1
        for nn in range(10):
            if '#'==s[nn] and c_flag == 0:
                c_flag = 1
                C = nn
            if '.'==s[nn] and c_flag == 1:
                D = nn-1
                c_flag = 0
    if '#' not in s and a_flag == 1:
        B = n-1
        a_flag = 0

if B == -1:
    B = 9
if D == -1:
    D = 9

print(A+1,B+1)
print(C+1,D+1)
