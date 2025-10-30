# 2580. 스도쿠

"""
시간 제한 1초, 메모리 제한 256MB

3. 완전탐색
    빈칸마다 1~9 대입
"""
# import sys
# sys.stdin = open('input.txt')

board = [list(map(int, input().split())) for _ in range(9)]

def is_possible(r, c, key):
    """빈칸 (r, c)에 해당 숫자 (key)를 넣는 게 가능/불가능한지 여부를 반환한다."""
    # 행
    for j in range(9):
        if board[r][j] == key:
            return False

    # 열
    for i in range(9):
        if board[i][c] == key:
            return False

    # 3x3 박스
    r_start = (r // 3) * 3
    c_start = (c // 3) * 3

    for i in range(r_start, r_start + 3):
        for j in range(c_start, c_start + 3):
            if board[i][j] == key:
                return False
    return True


def dfs(i):
    """빈칸인 경우, 후보 숫자들을 차례로 대입해본다."""
    # 마지막까지 무사히 대입했다면, 결과 출력 후 종료
    if i == len(blanks):
        for row in board:
            print(*row)
        exit(0)

    r, c = blanks[i]

    # 후보 숫자들을 하나씩 대입
    for num in range(1, 10):
        if is_possible(r, c, num):
            board[r][c] = num
            dfs(i + 1)
            board[r][c] = 0


# 모든 칸을 순회하면서 빈칸의 좌표를 저장한다.
blanks = []
for r in range(9):
    for c in range(9):
        if board[r][c] == 0:
            blanks.append((r, c))

dfs(0)