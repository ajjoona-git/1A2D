# 5202. 화물 도크

"""
최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 할 때, 화물차의 수
앞작업의 종료와 동시에 다음 작업을 시작할 수 있다.
=> 활동 선택 문제

1. 작업 종료시간이 빠른 순으로 정렬
"""

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    # [[작업 시작 시간, 작업 완료 시간], ...]
    work_hour = [[] for _ in range(N)]
    for i in range(N):
        work_hour[i].extend(map(int, input().split()))
    # 작업 종료 시간이 빠른 순으로 정렬
    work_hour.sort(key=lambda x:x[1])

    now_working = 0  # 앞 작업의 종료 시각
    count = 0  # 화물차의 수
    for s, e in work_hour:
        # 앞 작업의 종료시각보다 현재 작업의 시작시각이 먼저인 경우
        if s < now_working:
            continue
        # 현재 작업을 시작한다.
        count += 1
        now_working = e
    
    print(f'#{tc} {count}')
