# 4881. 배열 최소 합

from itertools import permutations

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 배열 최소합
    min_sum = float('inf')

    # 순열로 nPn
    for perm in permutations(range(N), N):
        # 현재 선택한 값들의 합
        current_sum = 0
        
        # perm 예시: [0, 2, 1, 3, 4, .. , N-1]
        # perm[r]는 r번째 행에서 선택하는 값의 인덱스를 의미한다.
        for i in range(N):
            current_sum += arr[i][perm[i]]
            # 현재합이 배열 최소합을 넘어간다면 더 계산하지 않는다.
            if current_sum > min_sum:
                break
        # 모든 행을 계산했다면 배열 최소합을 갱신한다.
        else:
            if current_sum < min_sum:
                min_sum = current_sum
        
    print(f'#{tc} {min_sum}')