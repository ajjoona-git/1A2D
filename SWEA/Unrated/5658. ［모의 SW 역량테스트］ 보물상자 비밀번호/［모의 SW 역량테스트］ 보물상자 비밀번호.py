# 5658. 보물상자 비밀번호

'''
네 변에 16진수 숫자(0~F)가 적혀 있는 보물상자가 있다.
보물 상자의 뚜껑은 시계방향으로 돌릴 수 있고, 
한 번 돌릴 때마다 숫자가 시계방향으로 한 칸씩 회전한다.
보물 상자에 적힌 숫자로 만들 수 있는 모든 수 중, K번째로 큰 수를 10진수로 만든 수
크기 순서를 셀 때 같은 수를 중복으로 세지 않도록 주의한다.

- 만들 수 있는 모든 수를 저장 -> set()
1. 인덱스 포인터 [원형 큐]
    - 한 변에 적힌 숫자의 개수 = N // 4 -> (N//4)회전하면 0회전과 동일
    - 시작 인덱스 = (직전 인덱스 - 1) % N 
2. 시계방향으로 회전 -> pop, insert(0)/appendleft
3. 회전 -> deque.rotate()
'''


def get_numbers():
    """만들 수 있는 모든 수를 10진수로 저장한 집합을 반환한다."""
    numbers = set()  # 만든 숫자를 저장
    side_len = N // 4  # 한 변의 길이

    for _ in range(side_len):
        for idx in range(0, N, side_len):
            hex_str = ''.join(passwords[idx:idx+side_len])
            numbers.add(int(hex_str, 16))
        passwords.insert(0, passwords.pop())
    
    return numbers


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    passwords = [i for i in input()]

    numbers = get_numbers()
    numbers_list = sorted(numbers, reverse=True)
    result = numbers_list[K-1]

    print(f'#{tc} {result}')