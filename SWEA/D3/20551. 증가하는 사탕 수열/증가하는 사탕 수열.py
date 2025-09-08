# 20551. 증가하는 사탕 수열

T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    candy = 0

    if A < B < C:
        pass

    elif B <= 1 or C <= 1:
        candy = -1

    else:
        if B >= C:
            candy += (B - C + 1)
            B = C - 1
        if A >= B:
            candy += (A - B + 1)
            A = B - 1
    
    print(f'#{tc} {candy}')
