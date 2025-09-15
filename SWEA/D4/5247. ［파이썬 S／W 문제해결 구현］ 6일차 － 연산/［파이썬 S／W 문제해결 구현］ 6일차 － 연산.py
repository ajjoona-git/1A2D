# 5247. 연산

from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    # BFS를 위한 큐: (숫자, 연산 횟수)
    q = deque([(N, 0)])
    # 연산 결과로 나온 숫자들
    visited = {N}
    result = 0

    while q:
        num, count = q.popleft()
        
        # 종료 조건: M을 만듦
        if num == M:
            result = count
            break
        
        # 4가지 연산 수행
        # +1, -1, *2, -10 
        next_num = num + 1
        if 0 < next_num <= 1e6 and next_num not in visited:
            visited.add(next_num)
            q.append((next_num, count + 1))

        next_num = num - 1
        if 0 < next_num <= 1e6 and next_num not in visited:
            visited.add(next_num)
            q.append((next_num, count + 1))

        next_num = num * 2
        if 0 < next_num <= 1e6 and next_num not in visited:
            visited.add(next_num)
            q.append((next_num, count + 1))

        next_num = num - 10
        if 0 < next_num <= 1e6 and next_num not in visited:
            visited.add(next_num)
            q.append((next_num, count + 1))

    print(f'#{tc} {result}')