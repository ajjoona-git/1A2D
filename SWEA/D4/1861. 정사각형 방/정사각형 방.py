# 1861. 정사각형 방

# 델타 배열 (상하좌우)
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# def move(r, c, count):
#     global max_count, start

#     for i in range(4):
#         nr, nc = r + dr[i], c + dc[i]
#         if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == grid[r][c] + 1:
#             print(grid[r][c])
#             move(nr, nc, count + 1)
#             break
#     else:
#         if count >= max_count:
#             max_count = count
#             start = min(start, grid[r][c])
#             return
    

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_count = 0
    # start = N ** 2
    
    # 인접한 방에 현재 방번호보다 1 크다면, 리스트에 저장
    linked = [0] * (N ** 2 + 1)

    for r in range(N):
        for c in range(N):
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if not (0 <= nr < N and 0 <= nc < N):
                    continue

                if grid[nr][nc] == grid[r][c] + 1:
                    linked[grid[r][c]] = 1
                    continue
    
    # 최대로 연속되는 방의 개수 구하기
    num = 1
    start = 1
    while num < N ** 2:
        # 연속된 1의 수(count)
        count = 1
        if linked[num] == 1:
            while linked[num + count] == 1:
                count += 1
                # num += 1
            if count > max_count:
                max_count = count
                start = num
        num += count

    print(f'#{tc} {start} {max_count + 1}')
