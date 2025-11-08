# 1288. 새로운 불면증 치료법

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    # 각 자리수의 숫자(0~9)를 기록할 비트마스크
    numbers = 0
    count = 1

    while count > 0:
        current_number = N * count

        # 각 자리수를 순회면서 numbers에 반영한다.
        while current_number > 0:
            digit = current_number % 10
            current_number //= 10
            numbers |= (1 << digit)

        # 종료 시점: 0~9 모든 숫자를 봤을 때
        if numbers == (1 << 10) - 1:
            break

        count += 1

    print(f"#{tc} {N * count}")    