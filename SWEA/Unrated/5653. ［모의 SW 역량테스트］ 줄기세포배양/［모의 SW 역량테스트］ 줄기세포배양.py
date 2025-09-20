# 5653. 줄기세포배양

"""
초기 상태에서 줄기 세포들은 비활성 상태이며 생명력 수치가 X인 줄기 세포의 경우 X시간 동안 비활성 상태이고 X시간이 지나는 순간 활성 상태가 된다.
줄기 세포가 활성 상태가 되면 X시간 동안 살아있을 수 있으며 X시간이 지나면 세포는 죽게 된다.
세포가 죽더라도 소멸되는 것은 아니고 죽은 상태로 해당 그리드 셀을 차지하게 된다.

활성화된 줄기 세포는 첫 1시간 동안 상, 하, 좌, 우 네 방향으로 동시에 번식을 한다.
번식된 줄기 세포는 비활성 상태이다.
하나의 그리드 셀에는 하나의 줄기 세포만 존재할 수 있기 때문에 번식하는 방향에 이미 줄기 세포가 존재하는 경우 해당 방향으로 추가적으로 번식하지 않는다.
두 개 이상의 줄기 세포가 하나의 그리드 셀에 동시 번식하려고 하는 경우 생명력 수치가 높은 줄기 세포가 해당 그리드 셀을 혼자서 차지하게 된다.

---

1. 비활성 상태의 시간을 카운트다운하면서 기록할 2차원 배열 & 세포의 생명력을 기록할 2차원 배열(-> 죽은 세포는 -1으로 표기)
    - 배열의 크기를 정하고 시작할 수가 있을까?? K시간 후이면 최대 사방으로 K칸이니까,,,
        (N + 2*K) x (M + 2*K)

2. 활성 + 비활성 세포 좌표를 세트에 저장

3. BFS (deque)
    방문한 좌표 저장하는 visited(dict) = {time: set((r, c))}
    활성 세포 -> 델타 순회하면서 visited 추가
    - 생명력 수치(origin)
    - 활성/비활성까지 남은 시간(countdown)
"""
from collections import deque
# import sys
# sys.stdin = open('sample_input.txt')


# 델타 배열 정의 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def initialize_queue():
    # 초기 줄기세포 정보 저장
    init = []  

    for r in range(N):
        for c in range(M):
            # 존재한다면 데크에 추가, 방문 처리
            if origin[r][c]:
                # (현재 시간, r, c, 생명력 수치, 활성/비활성까지 남은 시간, 활성 상태 여부)
                init.append((0, r, c,  origin[r][c], origin[r][c], False))
                visited.add((r, c))

    # 생명력 수치가 높은 순서로 정렬
    init.sort(key=lambda x: x[3], reverse=True)

    return deque(init)  


def bfs():
    q = initialize_queue()
    alive_cells = 0

    while q:
        t, r, c, hp, countdown, is_activated = q.popleft()

        # 현재 시간이 K인 경우
        if t == K:
            # 현재 활성&비활성 상태인 세포의 개수를 +1
            if not is_activated or countdown > 0:
                alive_cells += 1
            continue
            

        # 1. 활성 상태 & countdown == 0 인 경우, 죽은 세포
        if is_activated and countdown == 0:
            continue

        # 2. 비활성 상태 & countdown이 남아있을 경우, countdown -1
        if not is_activated and countdown > 0:
            q.append((t + 1, r, c, hp, countdown - 1, is_activated))
            continue
        
        # 3. 비활성 상태 & countdown == 0 인 경우, 활성화 상태로 전환 후 번식
        elif not is_activated:
            q.append((t + 1, r, c, hp, hp - 1, True))

        # 4. 활성 상태 & countdown이 남아있는 경우, 번식
        else:
            q.append((t + 1, r, c, hp, countdown - 1, is_activated))

        # 델타 순회하면서 번식
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            # 방문한 좌표는 pass
            if (nr, nc) in visited:
                continue
            
            q.append((t + 1, nr, nc, hp, hp, False))
            visited.add((nr, nc))

    return alive_cells


T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    origin = [list(map(int, input().split())) for _ in range(N)]

    visited = set()
    alive_cells = bfs()
    print(f'#{tc} {alive_cells}')