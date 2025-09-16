# 5251. 최소 이동 거리
import heapq


def dijkstra():
    """dijkstra 알고리즘. 0번 지점에서 N번 지점까지 최소 거리를 계산한다."""
    INF = float('inf')
    distances = [INF] * (N + 1)
    
    # 0번 지점에서 출발
    distances[0] = 0
    pq = [(0, 0)]  # (거리, 노드 번호)

    while pq:
        cost, node = heapq.heappop(pq)

        # 한 번 방문한 좌표는 다시 계산하지 않는다.
        if distances[node] < cost:
            continue

        for next_node, next_cost in adj_list[node]:
            if cost + next_cost < distances[next_node]: 
                distances[next_node] = cost + next_cost
                heapq.heappush(pq, (distances[next_node], next_node))
    
    return distances[N]


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())

    adj_list = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj_list[s].append((e, w))  # 단방향

    print(f'#{tc} {dijkstra()}')