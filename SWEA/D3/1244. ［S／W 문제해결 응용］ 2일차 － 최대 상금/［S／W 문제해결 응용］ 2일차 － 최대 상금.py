# 1244. 최대 상금

# import sys
# sys.stdin = open("input.txt")


def swap_digit(cnt):
    global result
    number = int(''.join(cards))

    # 메모이제이션: 교환횟수와 숫자를 기록
    # 똑같은 횟수만큼 교환했을 때 값이 같다면, 대표값 하나만 계산하고 나머지는 버린다.
    if (cnt, number) in swap_cases:
        return
    swap_cases.add((cnt, number))

    # 종료조건: N번 교환했을 경우
    if cnt == int(N):
        result = max(result, number)
        return

    # 자리교환
    # 교환할 자리수를 두가지 고르고,
    for idx_1 in range(digit):
        for idx_2 in range(idx_1 + 1, digit):
            cards[idx_1], cards[idx_2] = cards[idx_2], cards[idx_1]
            swap_digit(cnt + 1)
            cards[idx_1], cards[idx_2] = cards[idx_2], cards[idx_1]


T = int(input())
for tc in range(1, T + 1):
    initial_number, N = input().split()
    digit = len(initial_number)
    cards = list(initial_number)

    # 반복되는 숫자 패턴을 저장하는 세트
    # { (교환횟수, 숫자) }
    swap_cases = set()
    result = 0

    swap_digit(0)

    print(f'#{tc} {result}')
