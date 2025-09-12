# 5208. 전기버스2 

def charge(station, count):
    global min_charge
    battery = batteries[station]

    if count >= min_charge:
        return

    if station + battery >= N:
        min_charge = min(min_charge, count)
        return
    
    for drive in range(battery, 0, -1):
        charge(station + drive, count + 1)


T = int(input())
for tc in range(1, T+1):
    input_list = list(map(int, input().split()))
    N = input_list[0]
    # 1 ~ N-1번 정류장의 배터리 용량
    batteries = [0] + input_list[1:]
    
    min_charge = N
    charge(1, 0)

    print(f'#{tc} {min_charge}')
