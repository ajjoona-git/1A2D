# 5203. 베이비진 게임

"""
0~9 숫자 카드 * 4세트, 6개 카드 뽑기
연속 같은 숫자 3개 이상이면 run, 같은 숫자 3개 이상이면 triplet
플레이어 1, 2가 교대로 한장씩 카드를 가져간다.
승자를 출력한다. 무승부이면 0을 출력한다.
"""

def check_win(count_arr):
    """주어진 카운팅 배열(count_arr)에서 run 혹은 triplet이 있는지 확인한다."""
    for i in range(10):
        if count_arr[i] >= 3:  # triplet
            return True
        if count_arr[i] > 0 and count_arr[i+1] > 0 and count_arr[i+2] > 0:   # run
            return True

    return False


T = int(input())
for tc in range(1, T+1):
    card_info = list(map(int, input().split()))

    # 카운팅 배열 생성 (0~9, 인덱스 10, 11은 사용 안 함)
    player1_count = [0] * 12
    player2_count = [0] * 12
    winner = 0

    for i in range(6):
        player1_count[card_info[i*2]] += 1
        player2_count[card_info[i*2 + 1]] += 1

        # 카드더미가 3장이 안되는 경우 확인할 필요 없음
        if i < 2:
            continue

        if check_win(player1_count):
            winner = 1
            break
        if check_win(player2_count):
            winner = 2
            break
    
    print(f'#{tc} {winner}')
        