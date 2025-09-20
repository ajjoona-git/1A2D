"""
1. 완전탐색
grid[r][c] = [power, dir]
그리드 전체 순회하면서
(nr, nc) 위치에 값이 있다면 충돌
  에너지 계산
  (r,c)랑 (nr,nc) 값 초기화
아무것도 없다면 이동
  r, c 갱신
  (r,c)랑 (nr,nc) swap
=> 언제 종료..??? 무한루프 (폐기)

2. 시간은 중요하지 않다. 충돌하는지만 확인하면 됨. 
원자 정보를 하나씩 pop하면서
같은 열, 같은 행에 있는값 확인
같은 열, 행에 있더라도 방향이 서로 반대되는지 확인
충돌가능성있는 원자들 중 가장 가까운 원소와 충돌하므로
충돌가능성있는 원자들을 저장할 때 거리값도 같이 저장

=> 수직으로 만나는건 어떻게 확인?
남아있는 원자들로 확인해봐야 하는데...
수평으로 만나는 것보다 수직으로 만나는게 빠른 경우를 고려하지 못하네 (폐기)

3. 두 원자의 dx, dy가 x=0, y=0, x=y, x=-y 위에 있다면 만난다.
=> 가까운 원자부터 확인해야 하는데, x좌표나 y좌표 순으로 정렬하자.
=> 두 개 조합 (1000C2)
만나는 애들을 리스트에 저장해두고 충돌에너지 계산
"""

def check_collision(i, j):
    """충돌 가능성 있는 원자쌍을 리스트(collidable_pairs)에 추가한다."""
    x1, y1, d1, _ = atoms[i]
    x2, y2, d2, _ = atoms[j]

    dx = x2 - x1  # x좌표 차이
    dy = y2 - y1  # y좌표 차이

    # x좌표가 같고, d1=상, d2=하인 경우
    if dx == 0 and d1 == 0 and d2 == 1:
        collidable_pairs.append((dy, i, j))
    
    # y좌표가 같고, d1=우, d2=좌인 경우
    elif dy == 0 and d1 == 3 and d2 == 2:
        collidable_pairs.append((dx, i, j))

    # 수직으로 만나는 경우
    elif dx == -dy and (d1, d2) in [(3, 0), (1, 2)]:
        collidable_pairs.append((dx * 2, i, j))
    
    elif dx == dy and (d1, d2) in [(3, 1), (0, 2)]:
        collidable_pairs.append((dx * 2, i, j))


def calculate_energy():
    """충돌 가능성 있는 원자쌍 중에서 충돌할 때 방출하는 에너지를 계산한다."""
    energy = 0

    # 충돌한 원자의 이동거리를 저장할 리스트
    # 동시에 3개 이상의 원자가 충돌할 경우를 고려하기 위함
    records = [0] * N

    for dist, i, j in collidable_pairs:
        e1, e2 = atoms[i][3], atoms[j][3]

        if records[i] == 0 and records[j] == 0:
            energy += e1 + e2
            records[i] = records[j] = dist
        elif records[i] == 0 and records[j] == dist:
            energy += e1
            records[i] = dist
        elif records[j] == 0 and records[i] == dist:
            energy += e2
            records[j] = dist

    return energy


T = int(input())
for tc in range(1, T+1):
    N = int(input())  # 원자 개수
    
    atoms = []
    for _ in range(N):
        # [x, y, 이동 방향, 보유 에너지]
        # 이동 방향은 상(0), 하(1), 좌(2), 우(3)
        atoms.append(list(map(int, input().split())))
    # x좌표 순서로 오름차순 정렬, x좌표가 같다면 y좌표 순서로 정렬
    atoms.sort(key=lambda x: (x[0], x[1]))

    # 충돌 가능성 있는 원자쌍을 저장할 리스트
    # (충돌까지 이동 거리 합, 원자1, 원자2)
    collidable_pairs = []
    for i in range(N):
        for j in range(i+1, N):
            check_collision(i, j)

    # 충돌까지의 거리가 짧은 순서로 정렬
    collidable_pairs.sort(key=lambda x: x[0])
    result = calculate_energy()

    print(f'#{tc} {result}')