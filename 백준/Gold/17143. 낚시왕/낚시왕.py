# 17143. 낚시왕

# 격자판의 크기 R x C, 상어의 수 M
R, C, M = map(int, input().split())

grid = [[-1] * (C + 1) for _ in range(R + 1)]  # 격자판
sharks = {}  # 상어의 정보
for id in range(1, M+1):
    r, c, s, d, z = map(int, input().split())
    grid[r][c] = id  # 해당 좌표에 상어의 아이디 기록
    sharks[id] = [r, c, s, d, z]  # [위치, 속력, 방향, 크기]

# 방향 벡터 (정지/상/하/우/좌)
dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, 1, -1]

# 방향 전환
def change_direction(d):
    if d % 2 == 0:
        return d - 1
    else:
        return d + 1

answer = 0

# 낚시꾼의 위치 col
for col in range(1, C + 1):
    # 1. 상어 잡기
    for row in range(1, R + 1):
        if grid[row][col] > 0:
            id = grid[row][col]
            # 잡은 상어의 크기 더하기
            answer += sharks[id][-1]
            # 잡은 상어 제거
            sharks.pop(id)
            # 격자판 초기화
            grid[row][col] = -1
            break

    # 마지막 열에서 상어를 잡으면 종료
    if col == C:
        break

    # 2. 상어 이동
    for shark in sharks:
        r, c, s, d, z = sharks[shark]
        # 현재 위치의 격자판은 초기화한다.
        grid[r][c] = -1

        # 반복되는 주기는 제외한다.
        if d <= 2:  # 상하 방향인 경우
            s %= 2 * (R - 1)
        else:  # 좌우 방향인 경우
            s %= 2 * (C - 1)

        # 속력만큼 이동한다.
        for _ in range(s):
            nr, nc = r + dr[d], c + dc[d]
            # 벽을 만나면 방향 전환 후 이동
            if nr <= 0 or nr > R or nc <= 0 or nc > C:
                d = change_direction(d)
                nr, nc = r + dr[d], c + dc[d]
            r, c = nr, nc

        # 이동 마친 후 정보 갱신
        sharks[shark] = [r, c, s, d, z]

    # 3. 격자판 갱신
    for id in range(1, M + 1):
        shark = sharks.get(id, None)
        if shark:
            r, c = shark[0], shark[1]
        else:
            continue

        # 한 칸에 상어 두 마리 이상인 경우
        if grid[r][c] > 0:
            # 더 큰 상어가 있다면 지금 상어를 삭제
            if sharks[grid[r][c]][-1] > shark[-1]:
                sharks.pop(id)
            # 더 작은 상어가 있다면 그 상어를 삭제
            else:
                sharks.pop(grid[r][c])
                grid[r][c] = id
        else:
            grid[r][c] = id

print(answer)