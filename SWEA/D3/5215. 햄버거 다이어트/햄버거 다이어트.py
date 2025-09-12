# 5215. 햄버거 다이어트

def dfs(index, score, calory):
    global max_score
    
    # 종료 조건: 칼로리가 L 초과
    if calory > L:
        return
    
    # 종료 조건: 모든 재료에 대해 포함 여부를 선택함
    if index >= N:
        max_score = max(max_score, score)
        return
    
    Ti, Ki = ingredients[index]
    # 1. 현재 재료를 선택한다.
    dfs(index + 1, score + Ti, calory + Ki)
    # 2. 현재 재료를 선택하지 않는다.
    dfs(index + 1, score, calory)


T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    ingredients = [list(map(int, input().split())) for _ in range(N)]

    max_score = 0
    dfs(0, 0, 0)
    print(f'#{tc} {max_score}')