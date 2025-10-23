# 15486. 퇴사 2

"""
시간 제한 2초, 메모리 제한 512MB

1 ≤ N ≤ 1,500,000
1 ≤ Ti ≤ 50, 1 ≤ Pi ≤ 1,000

현재까지의 최대 수익을 이후 모든 날에 적용하는 과정이 비효율적. (2중 for문)
현재까지의 최대 수익을 하나의 변수로 저장하자.

=> python3 시간초과, pypy3 오답

---

현재 날짜의 최대 수익을 다음 날로 전파
=> python3 시간초과, pypy3 런타임 에러 (IndexError)

"""

N = int(input())
daily_profit = [0] * (N + 1)  # 각 날짜까지 얻을 수 있는 최대 수익을 기록한다.
# today_profit = 0  # 현재 시점까지의 누적 최대 수익

# 상담 일정을 순회하면서
for day in range(N):
    term, profit = map(int, input().split())
    # 현재까지의 최대 수익과 어제까지의 최대 수익(daily_profit[day]은 아직 갱신 안 된 상태)을 비교해 갱신합니다.
    # today_profit = max(today_profit, daily_profit[day])
    # 현재 날짜의 최대 수익을 다음 날로 전파합니다.
    # 상담 처리보다 먼저 수행하여, 상담 여부와 관계없이 day까지의 최대 수익을 다음 날로 전달합니다.
    daily_profit[day + 1] = max(daily_profit[day + 1], daily_profit[day])

    # 상담 종료일(end_date)을 기준으로 수익을 계산합니다.
    end_date = day + term
    # 상담 종료일이 N일 이후라면 무시합니다.
    if end_date > N:
        continue

    # 상담 종료일에 얻을 수 있는 수익을 갱신합니다.
    daily_profit[end_date] = max(daily_profit[end_date], daily_profit[day] + profit)

    # print(daily_profit)

print(max(daily_profit))