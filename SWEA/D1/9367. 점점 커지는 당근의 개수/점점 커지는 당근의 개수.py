T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))  # 당근의 크기
    result = 1
    
    count = 1
    for i in range(1, N):
        if arr[i-1] < arr[i]:
            count += 1
        else:
            if result < count:
                result = count
            count = 1
            
    if result < count:
        result = count

    print(f'#{tc} {result}')