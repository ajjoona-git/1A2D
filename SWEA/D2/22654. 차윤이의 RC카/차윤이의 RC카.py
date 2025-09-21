"""
'G' : RC카가 이동 가능한 땅
'T' : RC카가 이동이 불가능한 나무
'X' : 현재 RC카의 위치
'Y' : RC카를 이동 시키고자 하는 위치

RC카의 조종기로는 아래의 동작들을 할 수 있다.
'A' : 앞으로 이동 - 나무가 있는 곳이나 필드를 벗어나는 경우에는 아무 일도 일어나지 않는다.
      (RC카가 망가지는것을 방지하고자 장애물 판단 시스템이 탑재되었다.)
'L' : 현재 바라보고 있는 방향에서 왼쪽으로 90도 회전
'R' : 현재 바라보고 있는 방향에서 오른쪽으로 90도 회전

차윤이는 RC카를 항상 위를 바라보는 방향으로 부터 조종을 시작한다.
차윤이가 RC카를 조종한 커맨드가 주어졌을 때, 목적지에 도달 할 수 있는지 구하라. 
(커맨드가 종료되었을 때, 목적지에 위치 해 있어야 한다.)
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    field = [list(input().strip()) for _ in range(N)]
    Q = int(input())
    commands = [list(input().split()) for _ in range(Q)]

    
    # 출발, 도착 위치 찾기
    for r in range(N):
        for c in range(N):
            if field[r][c] == 'X':
                start = (r, c)  # 현재 위치
                break

    # 방향 설정 (상, 우, 하, 좌 / 시계 방향 순)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    result = [0] * Q

    # RC카 이동
    for i in range(Q):
        dir = 0  # 처음에는 위를 바라봄 (상)
        r, c = start
        
        for action in commands[i][1]:
            if action == 'L':
                dir = (dir - 1) % 4

            elif action == 'R':
                dir = (dir + 1) % 4
            
            else:
                nr = r + dr[dir]
                nc = c + dc[dir]
                if 0 <= nr < N and 0 <= nc < N and field[nr][nc] != 'T':
                    r, c = nr, nc
                    
        if field[r][c] == 'Y':
            result[i] = 1

    print(f'#{tc}', *result)

