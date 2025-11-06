# 9251. LCS

"""
시간 제한 2초, 메모리 제한 256MB
---
두 수열(최대 1000자) -> 모두의 부분 수열이 되는 수열 중 가장 긴 것

DP로 풀기
dp[i][j] = str1의 i번째 문자까지와 str2의 j번째 문자까지의 LCS 길이
"""

str1 = input().strip()
str2 = input().strip()

n1 = len(str1)
n2 = len(str2)

# 부분적인 LCS 길이를 기록
dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
        # 두 문자가 같은 경우, LCS에 포함된다.
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i-1][j-1] + 1
        # 두 문자가 다른 경우, 직전 길이(위쪽, 왼쪽) 중 더 큰 값으로 갱신한다.
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# 우하단의 값이 전체 LCS의 길이이다.
print(dp[n1][n2])
