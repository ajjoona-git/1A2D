# 5201. 컨테이너 운반

"""
M대의 트럭으로 N개의 컨테이너를 운반(A -> B)
트럭당 적재용량이 있고, 한 개의 컨테이너만 운반가능, 편도로 한 번만 운행
이동한 화물의 총 중량이 최대일 때, 옮겨진 화물의 전체 무게는?
화물을 싣지 못한 트럭이 있을 수도, 남은 화물이 있을 수도 있다.
컨테이너를 하나도 못 옮기는 경우 0을 출력

1. 화물 무게 오름차순 정렬, 트럭의 적재용량 내림차순 정렬
    트럭 하나씩 화물 배정(pop해서 적재용량 이내인지 확인)
    배정된 화물은 따로 누적 합
=> 8/10 오답

2. 화물 무게와 트럭의 적재용량이 같은 것부터 배정
    남은 트럭의 적재용량이 큰 것부터 1번 방법으로 배정
=> 7/10 오답

3. 1번에서 pop하는 게 아니라 확정된 화물만 제거할 것
=> 3/10 런타임에러
"""
# import sys
# sys.stdin = open("sample_input.txt")


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weights = sorted(list(map(int, input().split())), reverse=True)  # 화물의 무게(N)
    limits = sorted(list(map(int, input().split())), reverse=True)  # 트럭의 적재용량(M)
    used = [False] * N

    result = 0

    for i in range(M):
        for j in range(N):
            # container는 현재 트럭에 실을 수 있는 최대 용량의 화물
            container = weights[j]
            if not used[j] and container <= limits[i]:
                used[j] = True
                result += container
                break

    print(f'#{tc} {result}')