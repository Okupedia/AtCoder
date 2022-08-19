def reverse_check(num, flag):
    ans = 0
    if flag:
        if num == 0:
            ans =1
        return ans
    return num


N = int(input())
A = list(map(int,input().split()))

pointer_L=0
pointer_R=N-1

reverse_flag=0

# 操作Aと操作Bを逆転した操作を考えて、完成から空列にできるかどうか考える
    #操作A：x の要素をすべて flip する．つまり，0 ならば 1 に変え，1 ならば 0 に変える． その後，x の先頭に 0 を追加する．
    #→操作a:先頭の0を外してbit反転
    #操作B： x の末尾に 0 を追加する．
    #→操作b:おしりの0を外す

while pointer_L <= pointer_R:
    #bit反転が起きるたびに配列全てを書き換えると計算量が多すぎてダメ
    #分岐の条件には両端しか関与しないのなら、「今反転が起きている状態かどうか」をflagとして残しておいて、分岐するときだけ見てあげれば十分
    number_L = reverse_check(A[pointer_L], reverse_flag)
    number_R = reverse_check(A[pointer_L], reverse_flag)
    
    #操作aをした結果bができなくなることがあり得る
    #操作bを優先的に行うようにすればOK

    if number_R == 0:
        pointer_R-=1
    elif number_L == 0:
        pointer_L+=1
        if reverse_flag == 0:
            reverse_flag  = 1
        else:
            reverse_flag  = 0
    else:
        print('No')
        exit()

print('Yes')


