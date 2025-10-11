from collections import defaultdict

def solution(gems):
    # 전체 보석 종류의 수
    num_unique_gems = len(set(gems))
    n = len(gems)
    
    # 정답을 저장할 변수 (가장 긴 구간으로 초기화)
    answer = [1, n]
    min_len = n + 1  # 나올 수 없는 큰 값으로 초기화
    
    # 투 포인터와 보석 개수를 셀 딕셔너리 초기화
    start, end = 0, 0
    gem_counts = defaultdict(int)
    
    while end < n:
        # 1. 윈도우 확장: end 포인터를 오른쪽으로 이동하며 보석을 추가
        gem_counts[gems[end]] += 1
        
        # 2. 윈도우 축소: 모든 종류의 보석을 포함했다면 start를 이동
        while len(gem_counts) == num_unique_gems:
            current_len = end - start + 1
            
            # 현재 구간이 기존 최소 길이보다 짧으면 정답 갱신
            if current_len < min_len:
                min_len = current_len
                answer = [start + 1, end + 1]
            
            # start 포인터가 가리키는 보석을 윈도우에서 제거
            left_gem = gems[start]
            gem_counts[left_gem] -= 1
            
            # 만약 해당 보석의 개수가 0이 되면 딕셔너리에서 완전히 삭제
            if gem_counts[left_gem] == 0:
                del gem_counts[left_gem]
            
            # start 포인터를 오른쪽으로 이동
            start += 1
            
        # 다음 구간 탐색을 위해 end 포인터 이동
        end += 1
            
    return answer