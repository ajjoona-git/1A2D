# 1865. 동철이의 일 분배


# import sys
# sys.stdin = open("input.txt")


def get_percent(i, percent=1):
    """
    N명의 직원에 대해서 주어진 일이 모두 성공할 확률을 재귀 호출하며 계산하는 함수
    - Args
        i: 현재 순서에서 일을 할당할 직원 (0번 직원부터 N-1번 직원까지)
        percent: 개별 확률을 곱해나갈 것이므로 1로 초기화한다.
    """
    global max_percent

    # 확률(<=1.0)은 곱할수록 작아지기 때문에
    # 현재까지 계산한 확률이 max_percent보다 작다면 종료한다.
    if percent <= max_percent:
        return
         
    # N명의 직원에게 일을 배분했다면 max_percent를 갱신하고 종료한다.
    if i == N:
        if max_percent < percent:
            max_percent = percent   
        return

    # i번 직원에게 j번 일을 할당한다.
    for j in range(N):
        # 이미 할당된 일이면 넘어가고,
        if allocated[j]:
            continue
        # 할당되어 있지 않은 일이라면, 확률을 계산한다.
        else:
            allocated[j] = True
            get_percent(i + 1, percent * P[i][j] * 0.01)
            # backtracking을 위해 할당을 취소한다. 
            # (다른 직원에게 할당될 수 있도록)
            allocated[j] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 직원의 수
    # P[i][j] : i번 직원이 j번 일을 하면 성공할 확률(%)
    P = [list(map(float, input().split())) for _ in range(N)]

    # 할당된 일이면 True
    allocated = [False] * N
    
    # N명의 직원에 대하여, 주어진 일이 모두 성공할 확률의 최대값 (0.0 ~ 1.0)
    # (P[i][j]의 곱이 가장 큰 경우)
    max_percent = 0

    get_percent(0, 1)

    # 결과는 퍼센트 단위로 소수점 아래 7번째 자리에서 반올림하여 6번째까지 출력한다.
    print(f'#{tc} {max_percent * 100:.6f}')