# 1953. 탈주범 검거
# bfs로 풀어보기

# delta: 상, 하, 좌, 우 이동을 위한 델타
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# tunnels: 터널 구조물 타입별로 이동가능한 델타 인덱스를 저장함
tunnels = {
    '1': [0, 1, 2, 3],  # 상하좌우
    '2': [0, 1],  # 상하
    '3': [2, 3],  # 좌우
    '4': [0, 3],  # 상우
    '5': [1, 3],  # 하우
    '6': [1, 2],  # 하좌
    '7': [0, 2],  # 상좌
}

# connected: 상하좌우로 이동했을 때 연결가능한 터널 구조물 타입
connected = {
    0: ['1', '2', '5', '6'],  # 상
    1: ['1', '2', '4', '7'],  # 하
    2: ['1', '3', '4', '5'],  # 좌
    3: ['1', '3', '6', '7'],  # 우
}


def bfs(start_x, start_y):
    """(start_x, start_y)에서 출발해서 인접한 요소들을 너비 우선 탐색한 후,
        visited의 값이 L 이하인 노드 수를 반환하는 함수"""
    # visited: 방문여부를 표시함과 동시에 몇 시간 경과 후 방문했는지를 저장한다.
    # (시작점은 1, 시작점의 인접점은 2, ...)
    visited = [[0] * M for _ in range(N)]

    # q: 탐색할 정점을 저장할 큐
    q = []
    
    # 시작점에 대한 초기화
    q.append((start_x, start_y))
    visited[start_x][start_y] = 1

    # 큐에 입력되었던 노드 수
    count = 1

    # 큐가 비어 있지 않은 동안 반복한다.
    while q:
        # 현재 탐색할 정점을 디큐
        x, y = q.pop(0)

        # 종료 조건: L시간 경과 후 방문한 경우 탐색을 종료한다.
        if visited[x][y] >= L:
            break

        # (x, y)의 터널 구조물 타입의 이동 가능한 장소
        for i in tunnels.get(underground[x][y]):
            nx = x + delta[i][0]
            ny = y + delta[i][1]
            # (nx, ny)가 범위 안에 있으면서 방문하지 않았고 연결되어 있는 터널이면, 인큐
            if(
                0 <= nx < N and 0 <= ny < M
                and visited[nx][ny] == 0
                and underground[nx][ny] in connected[i]
            ):
                q.append((nx, ny))
                count += 1
                visited[nx][ny] = visited[x][y] + 1

    return count


T = int(input())
for tc in range(1, T+1):
    # N x M: 지하 터널 지도의 크기
    # (R, C): 맨홀 뚜껑의 위치(= 탈출 1시간 후의 위치)
    # L: 탈출 후 소요된 시간
    N, M, R, C, L = map(int, input().split())

    # underground: 지하 터널 지도 (NxM)
    underground = [input().split() for _ in range(N)]

    print(f'#{tc} {bfs(R, C)}')