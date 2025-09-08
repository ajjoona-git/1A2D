# 1249. 보급로
import heapq

# 이동 경로는 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
INF = 1e9  # 충분히 큰 수 (문제에서 도로 깊이의 범위를 안 줌)

def dijkstra(sr, sc):
    dist = [[INF] * N for _ in range(N)]

    dist[sr][sc] = 0
    pq = [(0, sr, sc)]

    while pq:
        curr_d, r, c = heapq.heappop(pq)

        # 종료조건: 도착지에 도착한 경우
        if (r, c) == (N-1, N-1):
            return dist[r][c]

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # 최소거리 갱신
            if (
                0 <= nr < N and 0 <= nc < N
                and curr_d + grid[nr][nc] < dist[nr][nc]
            ):
                dist[nr][nc] = curr_d + grid[nr][nc]
                heapq.heappush(pq, (dist[nr][nc], nr, nc))
                
    

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().strip())) for _ in range(N)]

    print(f'#{tc} {dijkstra(0, 0)}')