from itertools import combinations

def solution(n, q, ans):
    """
    0개인 조합이 있다면 숫자를 제외한다.
    n개 정수 중에서 만들 수 있는 5개 숫자 조합을 순회하면서
    가능한 조합을 찾는다.
    """
    # 숫자 조합에 사용할 정수 모음
    numbers = set(i for i in range(1, n + 1))
    
    # 0개인 조합은 숫자 조합에서 제외한다.
    for i, num in enumerate(ans):
        if num == 0:
            numbers -= set(q[i])
    
    m = len(ans)
    answer = 0
    
    # 5개 숫자 조합을 순회하면서
    for combo in combinations(numbers, 5):
        # 5가지 시도/정답을 비교한다.
        for i in range(m):
            # 교집합의 수가 정답 수와 일치하지 않는다면 비밀코드가 아니다.
            common = set(combo) & set(q[i])
            if len(common) != ans[i]:
                break
        # 5가지 모두 통과했다면 비밀코드다.
        else:
            answer += 1

    return answer