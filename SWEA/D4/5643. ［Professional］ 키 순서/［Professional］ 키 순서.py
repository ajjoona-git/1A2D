# 5643. 키 순서
from collections import defaultdict, deque
# import sys
# sys.stdin = open("sample_input.txt")


def traverse(adj_dict, node):
    """주어진 node를 루트노드로 하는 서브트리를 탐색한다.
        루트노드를 제외한 자손 노드의 수(n_count)를 반환한다."""
    q = deque()
    visited = [False] * (N + 1)

    q.append(node)
    visited[node] = True
    n_count = 0

    while q:
        v = q.popleft()
        for next_v in adj_dict.get(v, []):
            if visited[next_v]:
                continue
            visited[next_v] = True
            n_count += 1
            q.append(next_v)

    return n_count


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    M = int(input())

    # taller: 자식 노드번호 저장, smaller: 부모 노드번호 저장
    taller = defaultdict(list)
    smaller = defaultdict(list)

    for _ in range(M):
        s, t = map(int, input().split())
        taller[s].append(t)
        smaller[t].append(s)
    
    # 모든 학생에 대해 자신의 키순서를 알 수 있는지 여부를 검사
    # 자신보다 큰 학생의 수 + 자신보다 작은 학생의 수 == N - 1 이면 알 수 있다.
    result = 0
    for student in range(1, N+1):
        if traverse(taller, student) + traverse(smaller, student) == N - 1:
            result += 1

    print(f'#{tc} {result}')