from collections import defaultdict

#https://amateur-engineer-blog.com/union-find/より
class UnionFind():
    """
    Union Find木クラス

    Attributes
    --------------------
    n : int
        要素数
    root : list
        木の要素数
        0未満であればそのノードが根であり、添字の値が要素数
    rank : list
        木の深さ
    """

    def __init__(self, n):
        """
        Parameters
        ---------------------
        n : int
            要素数
        """
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self, x):
        """
        ノードxの根を見つける

        Parameters
        ---------------------
        x : int
            見つけるノード

        Returns
        ---------------------
        root : int
            根のノード
        """
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        """
        木の併合

        Parameters
        ---------------------
        x : int
            併合したノード
        y : int
            併合したノード
        """
        x = self.find(x)
        y = self.find(y)

        if(x == y):
            return
        elif(self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def same(self, x, y):
        """
        同じグループに属するか判定

        Parameters
        ---------------------
        x : int
            判定したノード
        y : int
            判定したノード

        Returns
        ---------------------
        ans : bool
            同じグループに属しているか
        """
        return self.find(x) == self.find(y)

    def size(self, x):
        """
        木のサイズを計算

        Parameters
        ---------------------
        x : int
            計算したい木のノード

        Returns
        ---------------------
        size : int
            木のサイズ
        """
        return -self.root[self.find(x)]

    def roots(self):
        """
        根のノードを取得

        Returns
        ---------------------
        roots : list
            根のノード
        """
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        """
        グループ数を取得

        Returns
        ---------------------
        size : int
            グループ数
        """
        return len(self.roots())

    def group_members(self):
        """
        全てのグループごとのノードを取得

        Returns
        ---------------------
        group_members : defaultdict
            根をキーとしたノードのリスト
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members


def return_black_index(black_grid_list, i, j):
    return_index = [-1, -1]
    if i-1 > 0:
        if black_grid_list[i-1][j] == 1:
            return_index[0] = i-1
            return_index[1] = j
        if j-1 > 0:
            if black_grid_list[i-1][j-1] == 1:
                return_index[0] = i-1
                return_index[1] = j-1
    if j-1 > 0:
        if black_grid_list[i][j-1] == 1:
            return_index[0] = i
            return_index[1] = j-1
    if i+1 < 1000:
        if black_grid_list[i+1][j] == 1:
            return_index[0] = i+1
            return_index[1] = j
        if j+1 < 1000:
            if black_grid_list[i+1][j+1] == 1:
                return_index[0] = i+1
                return_index[1] = j+1
    if j+1 < 1000:
        if black_grid_list[i][j+1] == 1:
            return_index[0] = i
            return_index[1] = j+1
    return return_index

black_grid_list = []
for i in range(2000):
    line = []
    for j in range(2000):
        line.append(0)
    black_grid_list.append(line)

N = int(input())

uf = UnionFind(20000000)

for n in range(N):
    x, y = map(int,input().split())
    x = x + 1000
    y = y + 1000
    black_grid_list[x][y] = 1
    print('x:',x, '/y:',y)
    #周辺をチェックする
    return_index = return_black_index(black_grid_list, x, y)
    if return_index[0] != -1:
        return_index_num = return_index[0] * 10000 + return_index[1]
        current_index_num = x * 10000 + y
        print('current_index_num:', current_index_num, 'return_index_num:', return_index_num)
        uf.unite(return_index_num, current_index_num)

print(uf.group_size())