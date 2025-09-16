# 5249. 최소 신장 트리
# prim - 정점 중심
import heapq

def prim(num_v, start):
    """start를 시작 정점으로 최소 신장 트리의 가중치 합을 구한다."""
    visited = [False] * num_v  # 0 ~ V번 노드의 방문 여부
    min_cost = 0  # MST의 총 가중치
    nodes_count = 0  # MST에 포함된 정점의 수
    pq = [(0, start)]  # 시작 노드 정보

    while pq:
        # 종료조건: 정점을 num_v개 뽑으면 MST 완성
        if nodes_count >= num_v:
            break

        cost, curr_node = heapq.heappop(pq)
        
        # 이미 방문했으면 스킵
        if visited[curr_node]:
            continue
        
        visited[curr_node] = True
        min_cost += cost
        nodes_count += 1

        for next_cost, next_node in adj_list[curr_node]:
            if not visited[next_node]:
                heapq.heappush(pq, (next_cost, next_node))

    return min_cost



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    
    adj_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        adj_list[n1].append((w, n2))
        adj_list[n2].append((w, n1))

    result = prim(V + 1, 0)
    print(f'#{tc} {result}')