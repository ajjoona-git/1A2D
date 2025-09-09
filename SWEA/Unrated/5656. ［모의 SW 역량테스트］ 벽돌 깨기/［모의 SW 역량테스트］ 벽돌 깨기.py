# 5656. 벽돌깨기

"""
구슬 N번 - 맨 위에 있는 벽돌만 깨트릴 수 있다.
-> 모든 위치에서 시도한다. N번 반복 (백트래킹)
    1 <= N <= 4
    2 <= W <= 12
    2 <= H <= 15

구슬이 명중한 벽돌은 상하좌우로 (벽돌에 적힌 숫자 -1)칸만큼 같이 제거. 연쇄작용.
-> BFS

- 백트래킹
    - 한번 쏘았을 때 벽돌들이 연쇄적으로 깨진다.
    - 현재 기준으로 퍼져나가면서 탐색(BFS)
    - 빈칸 메우기

- 가지치기
    - 최소 벽돌: 현재 벽돌이 다 깨지면 더 이상 할 필요 없다.
"""
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def gravity(arr):
    """중력이 작용해 빈 공간이 없어진 벽돌 상태를 반환한다."""
    # 각 열을 순회하면서
    for c in range(W):
        # 벽돌을 담을 큐 (선입선출)
        q = deque()
        for r in range(H - 1, -1, -1):
            # 벽돌이면 큐에 담고 0으로 초기화
            if arr[r][c] > 0:
                q.append(arr[r][c])
                arr[r][c] = 0
        # 밑(H-1)에서부터 벽돌을 쌓는다
        for idx in range(1, len(q) + 1):
            arr[H - idx][c] = q.popleft()


def bfs(r, c, arr, blocks):
    """한 번 구슬을 쏘았을 때 벽돌이 연쇄적으로 깨진 후 남은 벽돌의 수를 반환한다."""
    q = deque([(r, c, arr[r][c])])
    arr[r][c] = 0
    curr_blocks = blocks - 1

    while q:
        r, c, power = q.popleft()

        for p in range(1, power):
            for i in range(4):
                nr, nc = r + dr[i] * p, c + dc[i] * p
                if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] > 0:
                    q.append((nr, nc, arr[nr][nc]))
                    arr[nr][nc] = 0
                    curr_blocks -= 1

    return curr_blocks


def shoot(count, blocks, now_grid):
    """count 수만큼 구슬을 쏘고 남은 벽돌의 수를 계산하여 최소 벽돌을 갱신한다."""
    global min_blocks

    # 종료 조건
    if count == N or blocks == 0:
        min_blocks = min(min_blocks, blocks)
        return

    # 모든 열에 대해서 구슬쏘기
    for c in range(W):
        copy_grid = [row[:] for row in now_grid]

        # 맨 위에 있는 벽돌 찾기
        r = -1
        for idx in range(H):
            if copy_grid[idx][c] > 0:
                r = idx
                break
        # 해당 열에 벽돌이 없으면 통과
        if r == -1:
            continue

        curr_blocks = bfs(r, c, copy_grid, blocks)
        gravity(copy_grid)
        shoot(count + 1, curr_blocks, copy_grid)



T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]

    min_blocks = W * H
    blocks = 0
    for r in range(H):
        for c in range(W):
            if grid[r][c] > 0:
                blocks += 1
    
    shoot(0, blocks, grid)
    print(f'#{tc} {min_blocks}')