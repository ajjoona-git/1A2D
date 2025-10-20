# 2096. 내려가기

"""
python
시간 제한 1초, 메모리 제한 4MB

* Python에서 정수 객체 하나는 최소 28바이트를 차지한다.

dp 배열 = 100,000 * 3 * 2 * 28 bytes ~= 16,800,000 bytes ~= 16.8MB
grid 배열 = 100,000 * 3 * 28 bytes ~= 8.4MB
=> 이미 메모리 제한을 초과함...

1줄씩 불러오면서 계산하고 바로 dp에 저장함
"""

N = int(input())  # 행의 수

# 첫 번째 행 정보를 최대 점수, 최소 점수에 기록한다.
prev_row = list(map(int, input().split()))
max_dp = prev_row[:]
min_dp = prev_row[:]

# 한 줄씩 받아오면서 최대 점수, 최소 점수를 계산해간다.
for _ in range(N - 1):
    next_row = list(map(int, input().split()))

    # 계산한 최대, 최소 점수를 임시적으로 기록할 배열
    max_temp = [0] * 3
    min_temp = [0] * 3

    # i는 next_row의 인덱스
    for i in range(3):
        # 최대 점수 갱신
        max_temp[i] = next_row[i] + max(max_dp[j] for j in range(i - 1, i + 2) if 0 <= j <= 2)

        # 최소 점수 갱신
        min_temp[i] = next_row[i] + min(min_dp[j] for j in range(i - 1, i + 2) if 0 <= j <= 2)

    # 현재까지 계산한 점수를 이전 행으로 덮어쓰기
    max_dp = max_temp[:]
    min_dp = min_temp[:]

max_score = max(max_dp)
min_score = min(min_dp)

print(max_score, min_score)