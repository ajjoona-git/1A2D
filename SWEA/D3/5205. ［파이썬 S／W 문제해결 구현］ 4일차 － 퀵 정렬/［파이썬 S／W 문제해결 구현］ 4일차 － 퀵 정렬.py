# 5205. 퀵 정렬

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # 중앙값을 기준으로
    middle = [x for x in arr if x == pivot]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = quick_sort(arr)
    
    print(f'#{tc}', sorted_arr[N // 2])
