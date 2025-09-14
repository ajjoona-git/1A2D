# 2819. 격자판의 숫자 이어붙이기 


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def get_number(r, c, num_str, count):
    """7자리 숫자를 만들어 numbers 세트에 추가한다."""
    # 종료 조건: 7자리 수를 만들었을 때
    if count == 7:
        numbers.add(num_str)
        return
    
    # 가지치기: 현 위치에서 이미 같은 숫자를 만든 적이 있을 때
    if num_str in memo[r][c]:
        return
    else:
        memo[r][c].add(num_str)

    # 다음 자리 숫자를 찾아 이동
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            get_number(nr, nc, num_str + grid[nr][nc], count + 1)
        

T = int(input())
for tc in range(1, T+1):
    N = 4
    grid = [input().split() for _ in range(N)]

    numbers = set()
    memo = [[set() for _ in range(N)] for _ in range(N)]

    for r in range(N):
        for c in range(N):
            get_number(r, c, grid[r][c], 1)

    print(f'#{tc} {len(numbers)}')
