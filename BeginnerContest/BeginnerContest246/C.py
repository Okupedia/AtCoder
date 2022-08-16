N,K,X=map(int, input().split())
A = list(map(int, input().split()))

current_price_coupon_list = [[0,0],[0,0]]

for i in range(N):
    next_add_list = []#[次に加える価格,ここで使ったクーポンの枚数]
    next_add_prise = 9999
    next_price_coupon_list = []
    for k in range(K): 
        next_add_prise = A[i] - k*X
        if next_add_prise > 0:
            next_add_list.append([next_add_prise,k])
        else:
            next_add_list.append([0,k])
    for current_pair in current_price_coupon_list:
        for next_pair in next_add_list:
            if current_pair[1]+next_pair[1] <= K:
                next_price_coupon_list.append([current_pair[0]+next_pair[0],current_pair[1]+next_pair[1]])
    current_price_coupon_list = list(map(list, set(map(tuple, next_price_coupon_list))))
    # 高速化が必要な気がする
    # これもしかしてDPじゃない方が早い説

current_price_coupon_list.sort()
print(current_price_coupon_list[0][0])