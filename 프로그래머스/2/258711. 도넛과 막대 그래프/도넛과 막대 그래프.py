def solution(edges):
    # 각 정점의 진입/진출 차수를 계산 {node: [in, out]}
    in_out_degrees = {}
    for u, v in edges:
        in_out_degrees.setdefault(u, [0, 0])[1] += 1
        in_out_degrees.setdefault(v, [0, 0])[0] += 1
            
    answer = [0] * 4  # [생성 정점, 도넛, 막대, 8자]

    for node, [in_degree, out_degree] in in_out_degrees.items():
        # 생성 정점 찾기
        if out_degree >= 2 and in_degree == 0:
            answer[0] = node
            num_graphs = in_out_degrees[node][1]
        
        # 막대 모양 그래프
        elif out_degree == 0 and in_degree > 0:
            answer[2] += 1

        # 8자 모양 그래프
        elif out_degree == 2 and in_degree >= 2:
            answer[3] += 1
    
    # 도넛 모양 그래프
    answer[1] = num_graphs - answer[2] - answer[3]
        
    return answer