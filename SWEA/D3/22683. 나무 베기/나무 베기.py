# import sys
# sys.stdin = open('sample_input.txt')
"""
 N x N 크기의 필드 정보와 아빠가 벨 수 있는 최대 나무의 수가 주어졌을 때, 차윤이가 RC카를 목적지까지 이동시키기 위한 최소 조작 횟수를 구하라.
차윤이는 항상 위를 바라보는 상태로 RC카의 조작을 시작한다.
"""
from collections import deque

def find_x():
    # 출발 위치 찾기
    for r in range(N):
        for c in range(N):
            if field[r][c] == 'X':
                return r, c


# 방향 설정 (상, 우, 하, 좌 / 시계 방향 순)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# def dfs(r, c, dir, count, chance):
#     global result

#     # 종료 조건
#     if field[r][c] == 'Y':
#         result = min(result, count)
#         return
    
#     # 가지치기
#     if count >= result:
#         return

#     # RC카 이동
#     # 1. 'A'
#     nr = r + dr[dir]
#     nc = c + dc[dir]
#     if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
#         # 1-1. 전진
#         if field[nr][nc] != 'T':
#             visited[nr][nc] = 1
#             dfs(nr, nc, dir, count + 1, chance)

#         # 1-2. 나무 베고 전진
#         elif chance > 0:
#             field[nr][nc] = '.'
#             visited[nr][nc] = 1
#             dfs(nr, nc, dir, count + 1, chance - 1)
#             field[nr][nc] = 'T'
#             visited[nr][nc] = 0

    
#     # 2. 'L'
#     dfs(r, c, (dir - 1) % 4, count + 1, chance)

#     # 3. 'R'
#     dfs(r, c, (dir + 1) % 4, count + 1, chance)


def bfs():
    sr, sc = find_x()
    q = deque([(sr, sc, 0, 0, K)])

    # 딕셔너리 visited 정의: {(r, c, dir, chance): min_count}
    visited = {}
    visited[(sr, sc, 0, K)] = 0

    while q:
        r, c, dir, count, chance = q.popleft()

        if field[r][c] == 'Y':
            return count
            
        # if visited[r][c] >= result:
        #     continue

        # RC카 이동
        new_count = count + 1
        # 1. 'A'
        nr = r + dr[dir]
        nc = c + dc[dir]
        
        if 0 <= nr < N and 0 <= nc < N:
            # 1-1. 전진
            if field[nr][nc] != 'T':
                next_state = (nr, nc, dir, chance)
                if new_count < visited.get(next_state, float('inf')):
                    visited[next_state] = new_count 
                    q.append((nr, nc, dir, new_count, chance))

            # 1-2. 나무 베고 전진
            elif chance > 0:
                next_state = (nr, nc, dir, chance - 1)
                if new_count < visited.get(next_state, float('inf')):
                    visited[next_state] = new_count 
                    q.append((nr, nc, dir, new_count, chance - 1))

        # 2. 'L'
        next_state = (r, c, (dir - 1) % 4, chance)
        if new_count < visited.get(next_state, float('inf')):
            visited[next_state] = new_count
            q.append((r, c, (dir - 1) % 4, count + 1, chance))
        
        # 3. 'R'
        
        next_state = (r, c, (dir + 1) % 4, chance)
        if new_count < visited.get(next_state, float('inf')):
            visited[next_state] = new_count
            q.append((r, c, (dir + 1) % 4, count + 1, chance))

    return -1


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    field = [list(input().strip()) for _ in range(N)]

    result = bfs()

    print(f'#{tc} {result}')

