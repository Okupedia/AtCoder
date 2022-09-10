N = int(input()) #整数一つ

num = 998244353

div = int(N/num)

x = N
if N%num != 0:
    if div > 0:
        x = N - div * num
    elif div < 0:
        div -= 1
        x = N - div * num
    elif N < 0: #div = 0
        div -= 1
        x = N - div * num
    print(x)
else:
    print(0)