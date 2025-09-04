# 2115. 벌꿀채취

import itertools
# import sys
# sys.stdin = open("sample_input.txt")

def get_best_combo(r, c):
    """(r,c)부터 M개의 꿀통 중 C 이하의 꿀 조합을 반환하는 함수"""

    # 연속된 M개의 꿀통을 새로운 리스트로 만든다.
    workspace = honeycomb[r][c:c+M]
    best_profit = 0

    # M개를 모두 채취하는 경우부터 1개를 채취하는 경우까지
    for i in range(M, 0, -1):
        # i개 꿀을 선택할 때 만들 수 있는 모든 조합에 대해서
        for combo in itertools.combinations(workspace, i):
            # 꿀의 최대 양(C)를 넘는 경우를 제외한다.
            if sum(combo) > C:
                continue

            # 수익을 계산한다.
            profit = 0
            for honey in combo:
                profit += honey ** 2

            # 최대 수익을 넘는 경우 best_combo를 갱신한다.
            if profit > best_profit:
                best_profit = profit
    
    return best_profit


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    honeycomb = [list(map(int, input().split())) for _ in range(N)]
    max_profit = 0
    
    # 모든 위치에 대해서 첫 번째 조합을 만들고,
    for r1 in range(N):
        for c1 in range(N-M+1):
            profit1 = get_best_combo(r1, c1)
            
            # 해당 위치를 제외한 이후 위치에서의 두 번째 조합을 만든다.
            for r2 in range(r1, N):
                start_c2 = 0
                # 첫 번째 조합은 제외한다.
                if r2 == r1:
                    start_c2 = c1 + M
                for c2 in range(start_c2, N-M+1):
                    profit2 = get_best_combo(r2, c2)

                    # 최대 수익을 갱신한다.
                    if profit1 + profit2 > max_profit:
                        max_profit = profit1 + profit2

    print(f'#{tc} {max_profit}')

