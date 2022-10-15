from decimal import ROUND_HALF_UP, Decimal

X, K = map(int,input().split())


for i in range(1, K+1):
    x = Decimal(str(X))
    rank = '1E' + str(i)
    X = int(x.quantize(Decimal(rank), rounding=ROUND_HALF_UP))

print(int(X))