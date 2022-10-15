def function(k):
    if k == 0:
        return 1
    else:
        return k*function(k-1)

N = int(input())
print(function(N))
