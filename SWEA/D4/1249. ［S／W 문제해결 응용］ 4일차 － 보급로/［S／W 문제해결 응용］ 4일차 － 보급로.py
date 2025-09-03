import heapq
# import sys
# sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().strip())) for _ in range(N)]

    S = (0, 0)
    G = (N-1, N-1)

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 해당 좌표까지 최소 복구 시간을 저장할 리스트.
    dist = [[float('inf')] * N for _ in range(N)]
    hq = []

    dist[S[0]][S[1]] = 0
    heapq.heappush(hq, (0, 0, 0))

    while hq:
        cost, r, c = heapq.heappop(hq)

        # 최소보다 현재 비용이 크다면, 넘어감
        if cost > dist[r][c]:
            continue

        # 도착하면 종료
        if (r, c) == G:
            result = cost
            break

        # 인접 4방향 탐색
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # 경계 체크
            if 0 <= nr < N and 0 <= nc < N:
                ncost = cost + grid[nr][nc]
                if ncost < dist[nr][nc]:
                    dist[nr][nc] = ncost
                    heapq.heappush(hq, (ncost, nr, nc))

    print(f'#{tc} {result}')