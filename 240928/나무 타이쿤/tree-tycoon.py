import sys
input = sys.stdin.readline

dr = [0, -1, -1, -1, 0, 1, 1 ,1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
medi = [[n-1, 0], [n-2, 0], [n-1, 1], [n-2, 1]]
visited = set()

def move_medi() :
    d, p = map(int, input().split())
    for i in range(len(medi)) :
        medi[i][0] = (medi[i][0] + dr[d-1]*p) % n
        medi[i][1] = (medi[i][1] + dc[d-1]*p) % n

def grow() :
    grow_h = list()
    for r, c in medi :
        maps[r][c] += 1
    for i, (r, c) in enumerate(medi) :
        cnt = 0
        for j in range(1, 8, 2) :
            ar, ac = r + dr[j], c + dc[j]
            if -1 < ar < n and -1 < ac < n and maps[ar][ac] :
                cnt += 1
        grow_h.append(cnt)

    for i, (r, c) in enumerate(medi) :
        maps[r][c] += grow_h[i]
        visited.add((r,c))

def make_new_medi() :
    global medi, visited
    medi = list()
    for i in range(n) :
        for j in range(n) :
            if maps[i][j] >= 2 and (i, j) not in visited :
                maps[i][j] -= 2
                medi.append([i, j])
    visited = set()


for _ in range(m) :
    move_medi()
    grow()
    make_new_medi()
print(sum(map(sum, maps)))
출처: https://magentino.tistory.com/393 [마젠티노 IT개발스토리:티스토리]