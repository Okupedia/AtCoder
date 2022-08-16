N,K,X=map(int, input().split())
A = list(map(int, input().split()))

#A.sort()
#A.reverse()
A = sorted(A,reverse=True)

#print(A)

price_sum = 0
k_sum = 0

#初期の値がXより大きければ、0より小さくなるまで引いてあげたい
for i in range(N):
    k = 0
    a=A[i]
    if a > X:
        #=============================
        #枚ずつ使う実装だと遅い
        #10^18→1cesだと考えるべき
        #=============================
        #while k < K:
        #    k+=1
        #    a = a-X
        #    if a < 0:
        #        k-=1
        #        a += X
        #        break
        #=============================
        #kを求めるのは割り算でやった方がはやい
        # X*k <= aを満たすようなk枚を使うのが理想
        #=============================
        k = int(a/X)
        if k+k_sum > K:
            k = K - k_sum
        a = a-k*X
        #del A[0] #←これは、A[i+1]にあったものをA[i]にずらす、という作業を全ての要素に対してやるからめっちゃ遅い
        #A.append(a)
        A[i] = a
        k_sum += k
    else:
        break
    #print('k_sum :', k_sum, 'a : ', a)

#Xより小さい値について、ソートしなおす
A = sorted(A,reverse=True)
#print(A)
#print('=====sort=====')
for a in A:
    #クーポンがなくなるまで、一枚ずつつかっていく
    if k_sum < K:
        k_sum+=1
    else:
        price_sum += a
    #print('a :', a, 'k_sum :', k_sum, 'price_sum : ', price_sum)

print(price_sum)