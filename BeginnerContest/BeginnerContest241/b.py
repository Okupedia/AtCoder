N,M = input().split()
a = list(map(int, input().split())) #i本目の麺の長さ
b = list(map(int, input().split())) #i日目に食べたい麺の長さ

# bの項目が全てaに有れば大丈夫
for target in b:
    if target in a:
        a.remove(target)
    else:
        print("No")
        exit()
print("Yes")

