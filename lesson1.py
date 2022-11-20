from sys import maxsize

# start[m]: 辺mの始点番号
start = [0, 1, 2, 3, 4, 2, 5, 4, 6]
# end[m]: 辺mの終点番号
end = [0, 2, 3, 4, 1, 5, 4, 6, 2]
# edgefirst[n]: 点nの最初の接続辺の番号
edgefirst = [0, 1, 2, 3, 4, 6, 8]
# edgenext[m]: 辺mの次の接続辺の番号（ない場合は0）
edgenext = [0, 0, 5, 0, 7, 0, 0, 0, 0]
# searched[m]: 探索済みの経路番号の格納
searched = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# path[m]: 確定済みの経路を格納
path = [0, 0, 0, 0, 0, 0, 0, 0, 0]
# current[n]: 点nを始点とする未探索の辺の中で最小の番号を格納（ない場合は0を格納）
current = []

# 点の個数
N = 6
# 辺の個数
M = 8

# 各点での未探索の辺の番号の初期化
for i in range(N+1):
    current.append(edgefirst[i])

# 探索済みの経路の辺の格納位置を初期化
top = 1
# 確定済みの経路の辺の格納位置を初期化
last = M
# 出発点は点1
x = 1

