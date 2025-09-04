# 16811. 당근 포장하기


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))

    # 카운팅 배열 생성
    count_arr = [0] * 31
    for i in carrots:
        count_arr[i] += 1

    # 종료조건: 한 상자에 당근의 수는 N//2를 초과하면 안 된다.
    max_carrots = max(count_arr)
    capacity = N // 2
    if max_carrots > capacity:
        print(f'#{tc} {-1}')
        continue

    # 카운팅 배열에서 0인 항목 제거
    nonzero_counts = [count for count in count_arr if count != 0]
    nonzero_len = len(nonzero_counts)
    min_diff = float('inf')

    # 대/중/소 그룹을 구분할 칸막이의 인덱스
    for i in range(1, nonzero_len - 1):
        for j in range(i + 1, nonzero_len):
            small_carrots = sum(nonzero_counts[:i])
            medium_carrots = sum(nonzero_counts[i:j])
            large_carrots = sum(nonzero_counts[j:])

            # 조건: 한 상자에 당근의 수는 N//2를 초과하면 안 된다.
            max_carrot_count = max(small_carrots, medium_carrots, large_carrots)
            if max_carrot_count > capacity:
                continue

            # 개수 차이 갱신
            min_carrot_count = min(small_carrots, medium_carrots, large_carrots)
            min_diff = min(min_diff, max_carrot_count - min_carrot_count)

    # 포장 할 수 없는 경우 -1
    if min_diff == float('inf'):
        min_diff = -1

    print(f'#{tc} {min_diff}')
