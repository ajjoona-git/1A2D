# 1799. 비숍

'''오답
N = int(input())
# 비숍을 놓을 수 있는 곳에는 1, 비숍을 놓을 수 없는 곳에는 0
board = [list(map(int, input().split())) for _ in range(N)]
result = 0

for r in range(N):
    for c in range(N):
        # 비숍을 놓을 수 없는 곳은 pass
        if board[r][c] == 0:
            continue

        # 1이면 비숍을 놓는다.
        result += 1
        # 현 위치와 대각선 방향은 모두 비숍을 놓을 수 없기 때문에 0으로 바꾼다.
        board[r][c] = 0
        for i in range(r + 1, N):
            for j in range(N):
                dx = r - i
                dy = c - j
                if (dx == dy) or (dx == -dy):
                    board[i][j] = 0

print(result)
'''

''' 시간초과
def dfs(board, r, c, count):
    global max_count

    # 종료 조건: 모든 좌표를 정하면 종료
    if r == N:
        max_count = max(max_count, count)
        return

    # 1. 비숍을 놓는다.
    if board[r][c] == 1:
        # 현 위치와 대각선 방향은 모두 비숍을 놓을 수 없기 때문에 0으로 바꾼다.
        new_board = [row[:] for row in board]
        new_board[r][c] = 0
        for i in range(r + 1, N):
            for j in range(N):
                dx = r - i
                dy = c - j
                if (dx == dy) or (dx == -dy):
                    new_board[i][j] = 0

        if c+1 < N:
            dfs(new_board, r, c+1, count + 1)
        else:
            dfs(new_board, r+1, 0, count + 1)

    # 2. 비숍을 놓지 않는다.
    if c+1 < N:
        dfs(board, r, c+1, count)
    else:
        dfs(board, r+1, 0, count)


N = int(input())
# 비숍을 놓을 수 있는 곳에는 1, 비숍을 놓을 수 없는 곳에는 0
board = [list(map(int, input().split())) for _ in range(N)]
max_count = 0
dfs(board, 0, 0, 0)
print(max_count)
'''


''' 시간초과
# 대각선 위치를 탐색할 델타 배열
dr = [-1, -1, 1, 1]
dc = [-1, 1, -1, 1]


def dfs(r, c, count, blocked_positions=set()):
    global max_count

    if r == N:
        max_count = max(max_count, count)
        return

    # 비숍을 놓지 않는다.
    if c+1 < N:
        dfs(r, c+1, count, blocked_positions)
    else:
        dfs(r+1, 0, count, blocked_positions)

    # 비숍을 놓는다.
    if board[r][c] == 1 and (r, c) not in blocked_positions:
        new_blocked = {(r, c)}
        for i in range(4):
            for k in range(1, N):
                nr = r + dr[i] * k
                nc = c + dc[i] * k
                if 0 <= nr < N and 0 <= nc < N:
                    new_blocked.add((nr, nc))
        if c+1 < N:
            dfs(r, c+1, count+1, blocked_positions | new_blocked)
        else:
            dfs(r+1, 0, count+1, blocked_positions | new_blocked)


N = int(input())
# 비숍을 놓을 수 있는 곳에는 1, 비숍을 놓을 수 없는 곳에는 0
board = [list(map(int, input().split())) for _ in range(N)]

# 비숍을 놓을 수 없는 위치를 저장할 set
blocked_positions = set()

max_count = 0
dfs(0, 0, 0, blocked_positions)

print(max_count)
'''

''' 시간초과
def check(r, c):
    """(r, c) 위치에 비숍을 놓을 수 있는지 확인한다."""
    # 비숍을 놓을 수 없는 곳
    if board[r][c] == 0:
        return False

    # / 대각선에 비숍이 있는지 확인
    i, j = r - 1, c + 1
    while 0 <= i and j < N:
        if visited[i][j]:
            return False
        i -= 1
        j += 1

    # \ 대각선에 비숍이 있는지 확인
    i, j = r - 1, c - 1
    while 0 <= i and 0 <= j:
        if visited[i][j]:
            return False
        i -= 1
        j -= 1

    # 양 대각선에 비숍이 없다면 True
    return True


def dfs(r, c, count):
    global max_count

    # 종료 조건: 모든 좌표를 정하면 종료
    if r == N:
        max_count = max(max_count, count)
        return

    # 행 이동
    if c+1 < N:
        # 비숍을 놓는다.
        if check(r, c):
            visited[r][c] = 1
            dfs(r, c+1, count + 1)
            visited[r][c] = 0
        # 비숍을 놓지 않는다.
        dfs(r, c+1, count)

    # 열 이동
    else:
        # 비숍을 놓는다.
        if check(r, c):
            visited[r][c] = 1
            dfs(r+1, 0, count + 1)
            visited[r][c] = 0
        # 비숍을 놓지 않는다.
        dfs(r+1, 0, count)


N = int(input())
# 비숍을 놓을 수 있는 곳에는 1, 비숍을 놓을 수 없는 곳에는 0
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

max_count = 0
dfs(0, 0, 0)
print(max_count)
'''

# board = [[1] * N for _ in range(N)]


"""
흑과 백을 나눈다..?
r + c == 짝수 or 홀수
흑에서 시작하면 흑만 밟을 수 있음.
"""
''' 오답 (N이 짝수일 때, index + 2한다고 되지 않음)
def check_diagonal(r, c, visited):
    """(r, c) 위치에 비숍을 놓았을 때 대각선을 방문처리한다."""
    new_visited = [row[:] for row in visited]
    new_visited[r][c] = 1

    # / 좌하향 대각선
    i, j = r + 1, c - 1
    while i < N and 0 <= j:
        new_visited[i][j] = 1
        i += 1
        j -= 1

    # \ 우하향 대각선
    i, j = r + 1, c + 1
    while i < N and j < N:
        new_visited[i][j] = 1
        i += 1
        j += 1

    return new_visited


def dfs(index, count, visited):
    global max_count_odd, max_count_even

    r = index // N
    c = index % N

    # 종료 조건: 모든 좌표를 정하면 종료
    if index >= N ** 2:
        if index % 2 == 1:
            max_count_odd = max(max_count_odd, count)
        else:
            max_count_even = max(max_count_even, count)
        return
    
    # 가지치기: 현재값과 비숍을 놓을 수 있는 자리의 합이 max_count 이하라면 종료
    if index % 2 == 1:
        if count + board[index:].count(1) <= max_count_odd:
            return
        if count + sum(visited[i].count(0) for i in range(N)) <= max_count_odd:
            return
    else:
        if count + board[index:].count(1) <= max_count_even:
            return
        if count + sum(visited[i].count(0) for i in range(N)) <= max_count_even:
            return    

    # 비숍을 놓는다.
    if board[index] == 1 and visited[r][c] == 0:
        # blocked = []
        # 우하단 방향 대각선 (\)
        # blocked.extend([i for i in range(index, N ** 2, N + 1)])
        # 좌하단 방향 대각선 (/)
        # blocked.extend([i for i in range(index, N ** 2, N - 1)])
        # => 1차원 인덱스로 고려하면 반복이 끝나는 시점을 고려하지 못함
        
        new_visited = check_diagonal(r, c, visited)   
        dfs(index + 2, count + 1, new_visited)

    # 비숍을 놓지 않는다.
    dfs(index + 2, count, visited)

    # print(index, visited)


N = int(input())
board = [1] * (N ** 2)
# 비숍을 놓을 수 있는 곳에는 1, 비숍을 놓을 수 없는 곳에는 0
# board = []
# for _ in range(N):
#     board += list(map(int, input().split()))

max_count_odd, max_count_even = 0, 0

# visited: 비숍을 놓았거나 대각선 위치
visited = [[0] * N for _ in range(N)]
dfs(0, 0, visited)

visited = [[0] * N for _ in range(N)]
dfs(1, 0, visited)

print(max_count_odd, max_count_even)
'''


def check_diagonal(r, c, visited):
    """(r, c) 위치에 비숍을 놓았을 때 대각선을 방문처리한다."""
    new_visited = [row[:] for row in visited]
    new_visited[r][c] = 1

    # / 좌하향 대각선
    i, j = r + 1, c - 1
    while i < N and 0 <= j:
        new_visited[i][j] = 1
        i += 1
        j -= 1

    # \ 우하향 대각선
    i, j = r + 1, c + 1
    while i < N and j < N:
        new_visited[i][j] = 1
        i += 1
        j += 1

    return new_visited


# r + c % 2 == 1
def dfs_odd(r, c, count, visited):
    global max_count_odd

    # 종료 조건: 모든 좌표를 정하면 종료
    if r == N:
        max_count_odd = max(max_count_odd, count)
        return
        
    # 가지치기: 현재값과 비숍을 놓을 수 있는 자리의 합이 max_count 이하라면 종료
    if count + sum(board[i].count(1) for i in range(r, N)) <= max_count_odd:
        return
    if count + sum(visited[i].count(0) for i in range(r, N)) <= max_count_odd:
        return  

    # 비숍을 놓는다.
    if board[r][c] == 1 and visited[r][c] == 0:
        new_visited = check_diagonal(r, c, visited)   
        if c + 2 < N:  # 2칸 후
            dfs_odd(r, c + 2, count + 1, new_visited)
        elif (r + 1) % 2 == 0:  # 다음 행이 짝수번째이면 1번째 열부터
            dfs_odd(r + 1, 1, count + 1, new_visited)
        else:  # 다음 행이 홀수번째이면 0번째 열부터
            dfs_odd(r + 1, 0, count + 1, new_visited)

    # 비숍을 놓지 않는다.
    if c + 2 < N:  # 2칸 후
        dfs_odd(r, c + 2, count, visited)
    elif (r + 1) % 2 == 0:  # 다음 행이 짝수번째이면 1번째 열부터
        dfs_odd(r + 1, 1, count, visited)
    else:  # 다음 행이 홀수번째이면 0번째 열부터
        dfs_odd(r + 1, 0, count, visited)


# r + c % 2 == 0
def dfs_even(r, c, count, visited):
    global max_count_even

    # 종료 조건: 모든 좌표를 정하면 종료
    if r == N:
        max_count_even = max(max_count_even, count)
        return
        
    # 가지치기: 현재값과 비숍을 놓을 수 있는 자리의 합이 max_count 이하라면 종료
    if count + sum(board[i].count(1) for i in range(r, N)) <= max_count_even:
        return
    if count + sum(visited[i].count(0) for i in range(r, N)) <= max_count_even:
        return  

    # 비숍을 놓는다.
    if board[r][c] == 1 and visited[r][c] == 0:
        new_visited = check_diagonal(r, c, visited)   
        if c + 2 < N:  # 2칸 후
            dfs_even(r, c + 2, count + 1, new_visited)
        elif (r + 1) % 2 == 0:  # 다음 행이 짝수번째이면 0번째 열부터
            dfs_even(r + 1, 0, count + 1, new_visited)
        else:  # 다음 행이 홀수번째이면 1번째 열부터
            dfs_even(r + 1, 1, count + 1, new_visited)

    # 비숍을 놓지 않는다.
    if c + 2 < N:  # 2칸 후
        dfs_even(r, c + 2, count, visited)
    elif (r + 1) % 2 == 0:  # 다음 행이 짝수번째이면 0번째 열부터
        dfs_even(r + 1, 0, count, visited)
    else:  # 다음 행이 홀수번째이면 1번째 열부터
        dfs_even(r + 1, 1, count, visited)

    # print(r, c, visited)



N = int(input())
# board = [[1] * N for _ in range(N)]
# 비숍을 놓을 수 있는 곳에는 1, 비숍을 놓을 수 없는 곳에는 0
board = [list(map(int, input().split())) for _ in range(N)]


max_count_odd, max_count_even = 0, 0

# visited: 비숍을 놓았거나 대각선 위치
visited = [[0] * N for _ in range(N)]
dfs_odd(0, 1, 0, visited)

visited = [[0] * N for _ in range(N)]
dfs_even(0, 0, 0, visited)

print(max_count_odd + max_count_even)