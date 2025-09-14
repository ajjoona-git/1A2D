T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        if arr[i] == min(arr):
            min_idx = i
            break

    for i in range(N-1, -1, -1):
        if arr[i] == max(arr):
            max_idx = i
            break

    print(f'#{tc} {abs(min_idx - max_idx)}')