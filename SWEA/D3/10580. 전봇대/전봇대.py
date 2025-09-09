# 10580. 전봇대

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    wires = [tuple(map(int, input().split())) for _ in range(N)]

    # 현재 전선(a, b)에 대해 교차점은
    # 시작은 a보다 크고 끝은 b보다 작은 전선의 수만큼 생긴다.
    wires.sort(key=lambda x: x[0])
    count = 0
    for i in range(N):
        ai, bi = wires[i]
        for j in range(i+1, N):
            aj, bj = wires[j]
            if bi > bj:
                count += 1
    
    print(f'#{tc} {count}')