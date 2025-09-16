# 5250. 최소 비용 
import heapq


def dijkstra():
    """dijkstra 알고리즘. 각 노드까지 최소 연료 소비량을 계산한다."""
    INF = float('inf')
    cost_matrix = [[INF] * N for _ in range(N)]
    
    # 항상 출발은 맨 왼쪽 위
    pq = [(0, 0, 0)]  # (거리, r, c)
    cost_matrix[0][0] = 0
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while pq:
        cost, r, c = heapq.heappop(pq)

        # 도착지는 가장 오른쪽 아래
        # if (r, c) == (N-1, N-1):
        #     return cost
        
        # 한 번 방문한 좌표는 다시 계산하지 않는다.
        if cost_matrix[r][c] < cost:
            continue

        # 각 칸에서는 상하좌우 칸이 나타내는 인접 지역으로만 이동할 수 있다.
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                # 인접 지역으로 이동시에는 기본적으로 1만큼의 연료가 들고, 
                next_cost = cost + 1
                # 더 높은 곳으로 이동하는 경우 높이 차이만큼 추가로 연료가 소비된다.
                if grid[r][c] < grid[nr][nc]:
                    next_cost += (grid[nr][nc] - grid[r][c])
                    
                if next_cost < cost_matrix[nr][nc]:
                    cost_matrix[nr][nc] = next_cost
                    heapq.heappush(pq, (next_cost, nr, nc))
    
    return cost_matrix[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {dijkstra()}')