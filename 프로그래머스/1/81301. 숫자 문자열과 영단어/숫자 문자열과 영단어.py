numbers = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}


def solution(s):
    for key, value in numbers.items():
        if value in s:
            s = s.replace(value, str(key))
    return int(s)