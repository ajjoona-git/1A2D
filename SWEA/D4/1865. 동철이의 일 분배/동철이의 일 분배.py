# 1865. 동철이의 일 분배

# import sys
# sys.stdin = open("input.txt")

def get_max_possibility(emp_num, current_p):
    global result

    # 가지치기: 확률이 최대값보다 작다면 종료
    if current_p <= result:
        return

    # 종료조건: 모든 일을 배분했다면 최대값 갱신
    if emp_num == N:
        result = max(result, current_p)
        return

    # 남은 일 배분
    for task in range(N):
        if visited[task]:
            continue
        visited[task] = True
        get_max_possibility(emp_num + 1, current_p * P[emp_num][task])
        visited[task] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 직원과 할일의 인덱스는 0부터 N-1까지
    P = [list(map(lambda x: float(x) * 0.01, input().split())) for _ in range(N)]

    # 해야할 일이 배정되었는지 여부를 나타낸다.
    visited = [False] * N
    result = 0

    get_max_possibility(0, 1)

    print(f'#{tc} {result * 100:.6f}')
