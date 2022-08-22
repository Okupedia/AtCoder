X,Y,N = map(int,input().split()) #それぞれ別の変数

if X*3 > Y:
    apples_count = int(N/3)
    apple_count = N%3
    print(apples_count * Y + apple_count * X)
else:
    print(X * N)