# 1251. 하나로
# MST - prim
from heapq import heappop, heappush


def prim():
    pq = [(0, 0)]  # 0번 노드부터 시작
    visited = [0] * N  # 방문 여부
    min_cost = 0  # 최소 비용 합

    dist = [float('inf')] * N  # 최소 비용
    dist[0] = 0

    while pq:
        curr_cost, curr_node = heappop(pq)  

        # 이미 방문한 노드라면 pass
        if visited[curr_node]:
            continue

        visited[curr_node] = 1  
        min_cost += curr_cost

        for next_node in range(N):
            # 이미 방문한 노드라면 pass
            if visited[next_node]:
                continue
            
            # 환경 부담 세율(E)과 각 해저터널 길이(L)의 제곱의 곱(= E * L^2)
            next_cost = E * ((x_list[next_node] - x_list[curr_node]) ** 2 + 
                             (y_list[next_node] - y_list[curr_node]) ** 2)

            if next_cost < dist[next_node]:
                dist[next_node] = next_cost
                heappush(pq, (next_cost, next_node))

    return min_cost



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))
    E = float(input())

    min_cost = prim()
    print(f'#{tc} {min_cost:.0f}')
