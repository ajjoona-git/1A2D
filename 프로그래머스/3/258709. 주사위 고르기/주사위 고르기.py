def pick_dices(picked, index):
    """n/2개의 주사위 조합 고르기"""
    # n/2개 모두 고른 경우
    if len(picked) == N / 2:
        dice_combos.append(picked)
        return
    
    # 모든 주사위를 고려한 경우
    if index == N:
        return

    # 선택한다.
    pick_dices(picked + [index], index + 1)

    # 선택 안한다.
    pick_dices(picked, index + 1)
    

def calculate_sumation(dice, picked, total, index):
    """n/2개의 주사위에서 나올 수 있는 숫자의 합 모두 구하기"""
    if index == len(picked):
        sumations.append(total)
        return

    for face in dice[picked[index]]:
        calculate_sumation(dice, picked, total + face, index + 1)


def binary_search(arr, target):
    """정렬된 arr에서 target보다 작은 원소의 개수 구하기"""
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left

        
def solution(dice):
    global N, dice_combos, sumations
    N = len(dice)

    # 1. n/2개의 주사위 조합 고르기
    dice_combos = []
    pick_dices([], 0)

    results = []

    # 2. 각 주사위 조합을 순회하면서 숫자합 구하기
    #   절반만 순회하여 중복 계산 방지
    for comboA in dice_combos:
        sumations = []
        calculate_sumation(dice, comboA, 0, 0)
        sumationsA = sorted(sumations)

        comboB = [i for i in range(N) if i not in comboA]
        sumations = []
        calculate_sumation(dice, comboB, 0, 0)
        sumationsB = sorted(sumations)

        # 3. 숫자의 합이 더 큰 경우의 수 구하기
        wins = 0
        for valueA in sumationsA:
            wins += binary_search(sumationsB, valueA)

        # 4. (이기는 경우의 수, 주사위 조합) 저장
        results.append((wins, comboA))

    # 5. 경우의 수가 가장 큰 값 찾기
    _, combo = sorted(results, key=lambda x: x[0], reverse=True)[0]
    answer = [i + 1 for i in sorted(combo)]
    return answer