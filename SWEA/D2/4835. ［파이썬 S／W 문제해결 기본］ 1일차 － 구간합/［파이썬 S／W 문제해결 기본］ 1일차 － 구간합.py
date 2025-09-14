T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_sum, min_sum = sum(arr[:M]), sum(arr[:M])

    for i in range(1, N-M+1):
        curr_sum = 0
        for j in range(M):
            curr_sum += arr[i+j]
        min_sum = min(min_sum, curr_sum)
        max_sum = max(max_sum, curr_sum)

    print(f'#{tc} {max_sum - min_sum}')