from itertools import combinations

def check(number):
    num_str = str(number)
    n = len(num_str)

    for i in range(1, n):
        if num_str[i-1] > num_str[i]:
            return False
    return True


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = -1

    for a, b in combinations(arr, 2):
        if check(a * b) and a * b > result:
            result = a * b

    print(f'#{tc} {result}')