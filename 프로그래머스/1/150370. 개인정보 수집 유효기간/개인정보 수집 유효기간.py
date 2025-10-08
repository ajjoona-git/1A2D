def to_days(date):
    year, month, day = map(int, date.split('.'))
    return year * 12 * 28 + month * 28 + day


def solution(today, terms, privacies):
    answer = []
    
    # 약관별 일수를 딕셔너리 형태로 저장
    valid_days = {term[0]: 28 * int(term[2:]) for term in terms}

    for i, privacy in enumerate(privacies):
        date, contract = privacy.split()
        if to_days(date) + valid_days[contract] <= to_days(today):
            answer.append(i + 1)
            
    return answer