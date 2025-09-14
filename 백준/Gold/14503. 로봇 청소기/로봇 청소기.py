# 14503. 로봇 청소기

N, M = map(int, input().split())
r, c, d = map(int, input().split())
# 0: 청소되지 않은 빈 칸 / 1: 벽 / 2: 청소한 칸
grid = [list(map(int, input().split())) for _ in range(N)]

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

count = 0

while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if grid[r][c] == 0:
        grid[r][c] = 2
        count += 1

    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    for i in range(1, 5):
        # 반시계 방향으로 90도 회전한다.
        nd = (d - i) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]
        # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        if grid[nr][nc] == 0:
            r, c, d = nr, nc, nd
            break
    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    else:
        # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        nd = (d + 2) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]
        # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        if grid[nr][nc] == 1:
            break
        r, c = nr, nc

print(count)