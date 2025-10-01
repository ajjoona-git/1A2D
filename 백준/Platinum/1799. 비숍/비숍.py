import sys

def solve(index, count, bishops, visited_diag1, visited_diag2):
    """
    백트래킹을 통해 특정 색의 칸에 놓을 수 있는 비숍의 최대 개수를 찾는 함수
    
    Args:
        index (int): 현재 탐색할 수 있는 비숍 위치 리스트의 인덱스
        count (int): 현재까지 놓은 비숍의 개수
        bishops (list): 비숍을 놓을 수 있는 (r, c) 좌표 리스트
        visited_diag1 (list): '/' 방향 대각선 방문 여부
        visited_diag2 (list): '\' 방향 대각선 방문 여부
    """
    global max_count

    # 남은 칸에 모두 비숍을 놓아도 현재 최대값을 넘을 수 없으면 더 이상 탐색하지 않음 (가지치기)
    if len(bishops) - index + count <= max_count:
        return

    # 마지막 칸까지 탐색 완료
    if index == len(bishops):
        max_count = max(max_count, count)
        return

    r, c = bishops[index]

    # 현재 위치 (r, c)에 비숍을 놓을 수 있는지 확인
    # '/' 대각선 인덱스: r + c
    # '\' 대각선 인덱스: r - c + (n - 1)  (인덱스를 양수로 만들기 위해 n-1 더함)
    if not visited_diag1[r + c] and not visited_diag2[r - c + n - 1]:
        # 비숍을 놓는 경우
        visited_diag1[r + c] = True
        visited_diag2[r - c + n - 1] = True
        solve(index + 1, count + 1, bishops, visited_diag1, visited_diag2)
        
        # 백트래킹: 놓았던 비숍을 다시 회수
        visited_diag1[r + c] = False
        visited_diag2[r - c + n - 1] = False

    # 비숍을 놓지 않는 경우
    solve(index + 1, count, bishops, visited_diag1, visited_diag2)


# 입력 처리
n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 비숍을 놓을 수 있는 칸을 색깔별로 분리
white_bishops = []
black_bishops = []
for r in range(n):
    for c in range(n):
        if board[r][c] == 1:
            if (r + c) % 2 == 0:  # 흰색 칸 (체스판 기준)
                white_bishops.append((r, c))
            else:  # 검은색 칸
                black_bishops.append((r, c))

total_bishops = 0

# 1. 흰색 칸에 대해 최대 비숍 수 계산
max_count = 0
# 대각선 개수는 2*n - 1개
visited_diag1 = [False] * (2 * n - 1)
visited_diag2 = [False] * (2 * n - 1)
solve(0, 0, white_bishops, visited_diag1, visited_diag2)
total_bishops += max_count

# 2. 검은색 칸에 대해 최대 비숍 수 계산
max_count = 0
visited_diag1 = [False] * (2 * n - 1)
visited_diag2 = [False] * (2 * n - 1)
solve(0, 0, black_bishops, visited_diag1, visited_diag2)
total_bishops += max_count

print(total_bishops)