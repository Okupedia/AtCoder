N = int(input())
A = list(map(int,input().split()))
Q = int(input())

for q in range(Q):
    L,R,X=map(int,input().split)

#-------------------------
#Al~Arでxに等しいものを見つける
#値がxで、インデックスがl~rのものを探す
#→賢く探索
#   e.g. めぐる式二分探索
#-------------------------
