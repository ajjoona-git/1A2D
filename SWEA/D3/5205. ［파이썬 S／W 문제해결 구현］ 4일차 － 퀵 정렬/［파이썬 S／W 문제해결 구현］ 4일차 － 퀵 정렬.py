# 5205. 퀵 정렬

def partition(arr, start, end):
    # Lumoto 파티션 방식: 가장 마지막 원소를 피벗으로 설정
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[end] = arr[end], arr[i + 1]

    return i + 1


def quick_sort(arr, start, end):
    if start < end:
        # 1. 분할
        pivot_idx = partition(arr, start, end)

        # 2. 정복
        quick_sort(arr, start, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, end)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, N - 1)
    print(f"#{tc} {arr[N // 2]}")