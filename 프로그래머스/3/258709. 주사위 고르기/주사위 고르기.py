# 258709. 주사위 고르기
# Gemini 코드 - DP

# (유지) 주사위 조합을 고르는 함수는 기존과 동일합니다.
def pick_dices(picked, index, n, dice_combos):
    if len(picked) == n / 2:
        dice_combos.append(picked[:]) # 복사해서 추가
        return
    if index == n:
        return
    
    # 현재 주사위를 선택
    picked.append(index)
    pick_dices(picked, index + 1, n, dice_combos)
    picked.pop()
    
    # 현재 주사위를 선택하지 않음
    pick_dices(picked, index + 1, n, dice_combos)


# ✨ (개선) DP를 이용해 합계의 빈도수를 계산하는 함수
def calculate_sum_frequencies(combo, dice):
    """
    주어진 주사위 조합(combo)으로 만들 수 있는 모든 합의 빈도수를 계산합니다.
    예: {10: 1번, 12: 2번, 15: 1번}
    """
    # dp[합계] = 빈도수
    dp = {0: 1} # 초기값: 합계 0이 1번 나오는 경우로 시작

    for dice_index in combo:
        new_dp = {}
        # 기존 합계와 빈도수를 순회
        for prev_sum, count in dp.items():
            # 새로 추가된 주사위의 눈금을 순회
            for face in dice[dice_index]:
                current_sum = prev_sum + face
                # new_dp에 (새로운 합계)의 빈도수를 누적
                new_dp[current_sum] = new_dp.get(current_sum, 0) + count
        
        dp = new_dp # dp 테이블을 새로운 것으로 교체
    
    return dp


def solution(dice):
    n = len(dice)
    dice_combos = []
    pick_dices([], 0, n, dice_combos)

    max_wins = -1
    answer = []

    # 각 주사위 조합을 순회
    for comboA in dice_combos:
        comboB = [i for i in range(n) if i not in comboA]

        # ✨ (개선) 각 조합의 합계 빈도수를 DP로 계산
        freqA = calculate_sum_frequencies(comboA, dice)
        freqB = calculate_sum_frequencies(comboB, dice)

        # ✨ (개선) 투 포인터를 사용해 승리 횟수 계산
        
        # 각 플레이어의 합계를 오름차순으로 정렬
        sumsA = sorted(freqA.keys())
        sumsB = sorted(freqB.keys())
        
        current_wins = 0
        ptr = 0
        
        # 현재 sumA 값보다 작은 모든 sumB 값들의 총 빈도수 (sumA보다 작은 sumB의 총 등장 횟수)
        smaller_b_count = 0 

        # A의 합계를 기준으로 순회
        for sumA in sumsA:
            # B의 합계가 A의 합계보다 작을 동안 포인터(ptr) 이동
            while ptr < len(sumsB) and sumsB[ptr] < sumA:
                # B의 누적 경우의 수를 더해줌
                smaller_b_count += freqB[sumsB[ptr]]
                ptr += 1
            
            # (A가 이기는 경우) = (A의 현재 합 등장 횟수) * (현재 합보다 작은 B의 총 빈도수)
            current_wins += freqA[sumA] * smaller_b_count
        
        # 최대 승리 횟수 갱신
        if current_wins > max_wins:
            max_wins = current_wins
            answer = [i + 1 for i in comboA]

    return sorted(answer)