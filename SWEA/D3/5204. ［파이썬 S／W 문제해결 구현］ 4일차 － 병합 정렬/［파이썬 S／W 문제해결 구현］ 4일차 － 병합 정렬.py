# 5204. 병합 정렬

def merge(left_arr, right_arr):
    global count

    merged_arr = []
    left_idx, right_idx = 0, 0
    
    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] <= right_arr[right_idx]:
            merged_arr.append(left_arr[left_idx])
            left_idx += 1
        else:
            merged_arr.append(right_arr[right_idx])
            right_idx += 1
    
    # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수
    if left_idx < len(left_arr):
        count += 1

    merged_arr.extend(left_arr[left_idx:])
    merged_arr.extend(right_arr[right_idx:])

    return merged_arr
	
		
def merge_sort(arr):
    global count
		
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2  # 중앙 인덱스
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    count = 0
    sorted_arr = merge_sort(arr)
    
    print(f'#{tc} {sorted_arr[N//2]} {count}')
