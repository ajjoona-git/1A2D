# 10726. 이진수 표현

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    
    # 마지막 N 비트가 모두 1인 수
    mask = (1 << N) - 1
    
    # M의 이진수 표현의 마지막 N 비트가 모두 1로 켜져 있는지 아닌지를 판별
    if (M | mask) == M:
        print(f"#{tc} ON")
    else:
        print(f"#{tc} OFF")