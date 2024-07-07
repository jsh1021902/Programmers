def solution(n, costs):
    # set의 부모를 찾으면서 최종 부모로 연결도 해주는 함수
    def find_p(x):
        if x != forest[x][0]:
            forest[x][0] = find_p(forest[x][0])
        return forest[x][0]
    
    # 두 set의 rank를 비교해서 큰 쪽으로 union 해주는 함수
    def union(x, y):
        rank_x = forest[find_p(x)][1]
        rank_y = forest[find_p(y)][1]
        if rank_x >= rank_y:
            forest[find_p(y)][0] = find_p(x)
            rank_x += 1
        else:
            forest[find_p(x)][0] = find_p(y)
            rank_y += 1
    
    # [i는 parent, 0는 해당 set의 rank]
    forest = [[i, 0] for i in range(n)]
    
    # 비용을 기준으로 오름차순 정렬
    costs.sort(key = lambda x: x[2])
    
    # 총 비용
    total = 0
    
    for road in costs:
        # 두 섬이 연결되어있지 않으면 (부모가 다르면)
        if find_p(road[0]) != find_p(road[1]):
            # 연결(union)하고 총 비용에 해당 경로의 비용을 추가
            union(road[0], road[1])
            total += road[2]
    return total