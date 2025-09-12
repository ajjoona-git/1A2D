# 5209. 최소 생산 비용


def calculate_expense(product, expense):
    global min_expense
    # 가지치기: 현재 비용이 최소 비용 이상일 때
    if expense >= min_expense:
        return
    
    # 종료조건: 모든 제품(0~N-1)을 골랐다면
    if product >= N:
        min_expense = min(min_expense, expense)
        return
    
    # 공장선택
    for factory in range(N):
        if not visited[factory]:
            visited[factory] = True
            calculate_expense(product + 1, expense + arr[product][factory])
            visited[factory] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    min_expense = 100 * 15
    calculate_expense(0, 0)

    print(f'#{tc} {min_expense}')
