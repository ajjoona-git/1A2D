T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num_str = input()
    result = 0

    count = 0
    for n in num_str:
        if n == '1':
            count += 1
        else:
            count = 0
        
        if count > result:
            result = count

    print(f"#{tc} {result}")