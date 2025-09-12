# 1861. 정사각형 방

# 델타 배열 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def move(r, c):
    global max_count, start
    # 종료조건
    if visited[r][c] > 0:
        return visited[r][c]

    visited[r][c] = 1
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if (0 <= nr < N and 0 <= nc < N 
            and grid[nr][nc] == grid[r][c] + 1
        ):
            visited[r][c] += move(nr, nc)
            break

    return visited[r][c]
    

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    
    max_count = 0
    start = 0

    for r in range(N):
        for c in range(N):
            count = move(r, c)
            # 최대값 갱신
            if count > max_count:
                max_count = count
                start = grid[r][c]
            # 시작 방 번호 갱신
            elif count == max_count and grid[r][c] < start:
                start = grid[r][c]

    print(f'#{tc} {start} {max_count}')
