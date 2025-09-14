T = int(input())
for tc in range(1, T+1):
    N = int(input())
    bus_lines = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    stations = [int(input()) for _ in range(P)]

    # 1~5000번 버스 정류장에 몇 개의 버스가 다니는지 저장
    bus_stops = [0] * 5001

    for a, b in bus_lines:
        for stop in range(a, b+1):
            bus_stops[stop] += 1
    
    print(f"#{tc}", end=' ')
    for station in stations:
        print(bus_stops[station], end=' ')
    print()