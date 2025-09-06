#####solution.py
"""
양방향, 가중치 있는 그래프
경유지(최대 3개) 순서 상관없이 방문, 여러번 방문 가능, 
출발/도착도시 거쳐가도 ㄱㅊ, 경유지 아닌 다른 도시 거쳐도 ㄱㅊ,
경유지는 경로에 꼭 포함되어야 함

=> 다익스트라
	1. 노드 수(N개, 0 ~ N-1)만큼 1차원 배열 생성
		- 최대 중량(=최소 한도) 저장
		- INF로 초기화
	2. 출발노드부터 시작
		- 출발노드의 값은 0으로 초기화
		- 방문한 노드는 heapq에 heappush()
		- 현재 노드는 heappop()
		- 연결된 노드 방문 & 가중치 갱신: min(dij[curr], curr->next 가중치)
		- 방문 여부 검사하지 않아도 됨
		- (방문 여부 표시는 해야 됨) -> INF인 도시는 방문하지 않은 것
	3. 경유지와 출발, 도착도시를 모두 방문했다면 검사 끝

void init(int N, int K, int sCity[], int eCity[], int mLimit[])
for i -> K: node1, node2, weight = sCity[i], eCity[i], mLimit[i]
graph -> dict로 추가? {sCity: {(eCity, mLimit),},}
from collections import defaultdict
defaultdict(set)
	도시의 개수(node) 5 <= N <= 1000
	도로의 개수(edge) 2 <= K <= 2000
	(0 ≤ i ＜ K)인 모든 i에 대해,
	sCity[i]: 도로 i와 연결된 도시 ( 0 ≤ sCity[i] < N )
	eCity[i]: 도로 i와 연결된 도시 ( 0 ≤ eCity[i] < N )
	mLimit[i]: 도로 i를 이용할 수 있는 최대 중량 ( 1 ≤ mLimit[i] ≤ 30,000 )

void add(int sCity, int eCity, int mLimit)
양방향 도로를 추가한다.

int calculate(int sCity, int eCity, int M, int mStopover[])
sCity부터 M개의 경유지를 거쳐 eCity까지의 최대 중량(=최소 한도)을 반환한다.
이동이 불가능하다면 -1을 반환한다.
max_limit = -1 -> for permutations -> if limit == inf: continue
완전탐색? -> 순열(최대 3개니까 3중 for 문)
다익스트라로 출발지와 경유지에서 출발할 때의 가중치(min)를 모두 구하고
순열로 만든 경유지 순서대로 값을 골라와서 최대 중량(max)을 비교한다.
	mStopover: M개의 경유지 리스트
	1 <= M <= 3

시간복잡도 (6.5초 제한)
init	1 * K(2000) * O(1) * 2
add		1400 * O(1) * 2
calculate	100 * K(2000) * (M+1)(4) * M!(6)
= 약 480만 번
"""
import heapq
from collections import defaultdict

def init(N, K, sCity, eCity, mLimit):
	""" 초기 도로 정보를 입력받아 adj_list (list)에 저장한다.
	
	Args:
		N (int): 도시의 개수 ( 5 ≤ N ≤ 1,000 )
		K (int): 도로의 개수 ( 2 ≤ K ≤ 2,000 )
		(0 ≤ i ＜ K)인 모든 i에 대해,
		sCity[i] (list): 도로 i와 연결된 도시 ( 0 ≤ sCity[i] < N )
		eCity[i] (list): 도로 i와 연결된 도시 ( 0 ≤ eCity[i] < N )
		mLimit[i] (list): 도로 i를 이용할 수 있는 최대 중량 ( 1 ≤ mLimit[i] ≤ 30,000 )
	
	Examples:
		adj_list = { sCity: {(eCity, mLimit),}, eCity: {(sCity, mLimit),}, }
	"""
	global NUM_CITY, adj_list
	NUM_CITY = N
	adj_list = defaultdict(list)

	for i in range(K):
		add(sCity[i], eCity[i], mLimit[i])

	# print(adj_list)
	return


def add(sCity, eCity, mLimit):
	""" 인접 딕셔너리(adj_list)에 양방향 도로 정보를 추가한다.
	
	Args:
		sCity (int): 도로와 연결된 도시 ( 0 ≤ sCity < N )
		eCity (int): 도로와 연결된 도시 ( 0 ≤ eCity < N )
		mLimit (int): 도로를 이용할 수 있는 최대 중량 ( 1 ≤ mLimit ≤ 30,000 )
	"""
	adj_list[sCity].append((eCity, mLimit))
	adj_list[eCity].append((sCity, mLimit))
	return


def dijkstra(sCity):
	""" sCity에서 출발할 때 각 도시까지 운송할 수 있는 화물의 최대 중량을 반환한다.

	Args:
		N (int): 도시의 개수 ( 5 ≤ N ≤ 1,000 )
		sCity (int): 출발 도시 ( 0 ≤ sCity < N )

	Returns:
		(0 ≤ i ＜ N)인 모든 i에 대해,
		mLimit_list[i] ([int, set]): sCity에서 출발하여 i 도시에 도착할 때까지 운송할 수 있는 화물의 최대 중량과 경유지 정보
	"""
	global INF
	# 0. 결과 배열 선언
	mLimit_list = [-1] * NUM_CITY

	# 1. 출발 도시 초기화
	# 	 (최대)힙큐에는 (limit, city)를 추가
	INF = 30001
	q = [(-INF, sCity)]
	
	# 2. 큐가 빌 때까지(비어 있지 않은 동안) 반복 
	#  	 우선순위가 높은 순서대로 탐색을 진행한다.
	while q:
		cLimit, cCity = heapq.heappop(q)
		# print(cLimit, cCity)

		# 3. mLimit_list에 한도를 기록
		#    저장된 중량 한도가 -1이 아니라면, 이미 방문한 도시인 것
		if mLimit_list[cCity] != -1:
			continue
		mLimit_list[cCity] = -cLimit

		# 4. 연결된 모든 도시 방문
		# 	 현재 도시와 다음 도시를 연결하는 도로의 한도(nLimit)와 현재 도시까지의 최대 중량 한도(cLimit)를 비교해서 더 작은 값으로 갱신
		for nCity, nLimit in adj_list[cCity]:
			# print(nCity, nLimit)
			limit = min(-cLimit, nLimit)
			heapq.heappush(q, (-limit, nCity))
	# print(mLimit_list)
	return mLimit_list


def calculate(sCity, eCity, M, mStopover):
	""" sCity부터 M개의 경유지를 거쳐 eCity까지 운송가능한 화물의 최대 중량(=최소 한도)을 반환한다.
		이동이 불가능하다면 -1을 반환한다.

	- Args:
		sCity (int): 출발 도시 ( 0 ≤ sCity < N )
		eCity (int): 도착 도시 ( 0 ≤ eCity < N )
		M (int): 경유지 개수 ( 1 ≤ M ≤ 3)
		(0 ≤ i ＜ M)인 모든 i에 대해,
		mStopover[i] (int): 경유해야 되는 도시 ( 0 ≤ mStopover[i] < N )
	
	- Returns:
		maxLimit (int): 운송 가능한 화물의 최대 중량, 이동 불가능하다면 -1
	"""
	mLimit_list = dijkstra(sCity)
	mStopover.append(eCity)

	# 값이 INF라는 건 도로로 연결되지 않은 도시하는 뜻
	for stopover in mStopover:
		if mLimit_list[stopover] == INF:
			return -1
		
	maxLimit = min(mLimit_list[idx] for idx in mStopover)
	return maxLimit


	# { 출발 도시: 각 도시까지 운송할 수 있는 화물의 최대 중량 리스트 }
	# mLimit_dict = { sCity: dijkstra(sCity), }
	# # 각 경유지에 대해 계산한 최대 중량 리스트를 mLimit_dict에 추가
	# for stopover in mStopover:
	# 	mLimit_dict.update({stopover: dijkstra(stopover)})	

	# # 경유지를 경유하는 순서에 따라 최대 중량을 계산
	# if M == 1:
	# 	maxLimit = min(mLimit_dict[sCity][mStopover[0]], mLimit_dict[mStopover[0]][eCity])
	# 	return maxLimit if maxLimit < INF else -1
	
	# elif M ==2:
	# 	maxLimit = max(mLimit_dict[sCity][mStopover[0]], mLimit_dict[mStopover[0]][mStopover[1]], mLimit_dict[mStopover[1]][eCity])
		
			 
	# max_limit = -1 -> for permutations -> if limit == inf: continue
	# 완전탐색? -> 순열(최대 3개니까 3중 for 문)
	# 다익스트라로 출발지와 경유지에서 출발할 때의 가중치(min)를 모두 구하고
	# 순열로 만든 경유지 순서대로 값을 골라와서 최대 중량(max)을 비교한다.
