T = int(input())
for _ in range(T):
    p = input()  # 함수
    n = int(input())  # 배열의 길이
    input_str = input()  # 배열 [x1, ..., xn]

    # 함수만 보고 전처리하기
    # 1. D의 개수가 배열의 길이보다 크면 error
    if p.count("D") > n:
        print("error")
        continue
    # 2. "RR" 연속으로 있으면 원본이랑 똑같으므로 제거
    p = p.replace("RR", "")

    # 입력받은 배열 문자열을 리스트로 저장
    if n == 0:
        arr = []
    else:
        # arr = list(map(int, input_str.strip('[]').split(',')))
        arr = input_str.strip('[]').split(',')

    # 인덱스 포인터
    left, right = 0, n
    is_reversed = False
    is_error = False

    # 전처리된 함수를 순회하면서 명령 수행
    for command in p:
        # 순서 뒤집기 (R)
        if command == 'R':
            is_reversed = not is_reversed
        # 첫 번째 수 버리기 (D)
        elif command == 'D':
            # 배열이 비어있으면 error
            if left == right:
                is_error = True
                break

            if not is_reversed:  # 정방향
                left += 1
            else:  # 역방향
                right -= 1

    # 결과 출력하기
    if is_error:
        print("error")

    elif left == right:
        print("[]")

    else:  # 최종 배열 저장
        if not is_reversed:  # 정방향
            result = arr[left:right]
        else:  # 역방향
            result = arr[left:right]
            result.reverse()

        print(f"[{','.join(result)}]")
