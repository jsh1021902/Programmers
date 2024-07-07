def solution(routes):
    # 진출 지점에 대해서 오름차순 정렬
    routes.sort(key = lambda x: x[1])
    # 기준은 제한사항 참고
    key = -30001
    # 필요한 카메라 수
    cnt = 0
    
    for route in routes:
        # 기준(카메라)보다 진입지점이 뒤에 있으면
        if route[0] > key:
            # 단속이 안되기에 카메라 하나 더 필요
            cnt += 1
            # 새로운 기준은 해당 경로의 진출 지점 (맨 끝)
            key = route[1]
    return cnt