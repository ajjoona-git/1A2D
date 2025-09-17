# 4008. 숫자 만들기


def get_number(count, number):
    """모든 연산자로 만들 수 있는 수를 계산한다."""
    global min_number, max_number

    # 종료 조건: 연산자를 N-1개 고름
    if count == N - 1:
        min_number = min(min_number, number)
        max_number = max(max_number, number)
        return
    
    # 남아있는 연산자 중 하나를 고른다.
    for i in range(4):
        if cards[i] <= 0:
            continue
        
        # 연산자 카드 하나 소진
        cards[i] -= 1

        # 연산
        if i == 0:
            new_number = number + numbers[count + 1]
        elif i == 1:
            new_number = number - numbers[count + 1]
        elif i == 2:
            new_number = number * numbers[count + 1]
        else:
            new_number = int(number / numbers[count + 1])
        
        # 재귀 호출
        get_number(count + 1, new_number)
        # 백트래킹
        cards[i] += 1



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # '+', '-', '*', '/' 순서대로 연산자 카드의 개수
    cards = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    min_number, max_number = 1e8, -1e8

    get_number(0, numbers[0])

    print(f'#{tc} {max_number - min_number}')
