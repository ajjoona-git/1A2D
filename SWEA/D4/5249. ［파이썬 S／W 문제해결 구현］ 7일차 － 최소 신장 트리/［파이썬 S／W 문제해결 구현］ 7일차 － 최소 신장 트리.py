# 5249. 최소 신장 트리
# kruskal - 간선 중심

def find_set(parents, x):
    """x를 포함하는 집합의 대표자를 반환한다."""
    if parents[x] != x:
        parents[x] = find_set(parents, parents[x])
    return parents[x]


def union(parents, x, y):
    """두 원소 x, y를 같은 집합으로 합친다."""
    root_x = find_set(parents, x)
    root_y = find_set(parents, y)
    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y


def kruskal(num_v):
    """가중치가 작은 간선부터 선택하며 최소 신장 트리의 가중치 합을 구한다."""
    # 가중치를 기준으로 오름차순 정렬
    edges.sort(key=lambda x: x[2])

    min_cost = 0  # MST의 총 가중치
    edges_count = 0  # MST에 포함된 간선의 수
    parents = list(range(num_v))  # union-find를 위한 make_set
    
    for n1, n2, w in edges:
        # 사이클이 생긴다면 pass
        if find_set(parents, n1) == find_set(parents, n2):
            continue

        union(parents, n1, n2)
        min_cost += w
        edges_count += 1

        # 간선을 num_v-1개 선택했다면 MST 완성
        if edges_count == num_v - 1:
            break

    return min_cost


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    
    edges = [tuple(map(int, input().split())) for _ in range(E)]
    result = kruskal(V + 1)

    print(f'#{tc} {result}')