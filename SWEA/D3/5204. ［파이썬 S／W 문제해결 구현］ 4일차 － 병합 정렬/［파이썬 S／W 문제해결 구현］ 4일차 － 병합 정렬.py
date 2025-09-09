# 5204. 병합 정렬

def merge_sort(arr):
    global count
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2  # 중앙 인덱스
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수
    if left[-1] > right[-1]:
        count += 1

    merged_arr = []
    l = h = 0
    while l < len(left) and h < len(right):
        if left[l] < right[h]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[h])
            h += 1

    merged_arr += left[l:]
    merged_arr += right[h:]
    return merged_arr


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    count = 0
    sorted_arr = merge_sort(arr)
    
    print(f'#{tc} {sorted_arr[N//2]} {count}')
