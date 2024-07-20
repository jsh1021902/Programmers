from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    # 제한사항에서 모든 좌표값은 1 이상 50 이하라고 했고 2배의 좌표를 그려야 하므로 102*102 크기의 2차원 배열 선언
    field = [[-1] * 102 for i in range(102)]
    
    # 직사각형이 겹쳐진 다각형 그리기
    for r in rectangle:
    	# print(r) ------- 1
        
    	# 모든 좌표값 2배
        x1 = r[0] * 2
        y1 = r[1] * 2
        x2 = r[2] * 2
        y2 = r[3] * 2
        # x1부터 x2, y1부터 y2까지 순회 = 가로~가로, 세로~세로 순회
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
            	# x1, x2, y1, y2는 테두리이므로 제외하고 내부만 0으로 채움
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                # 다른 직사각형의 내부가 아니면서 테두리일 때 1로 채움
                elif field[i][j] != 0:    # else로 하면 에러남
                    field[i][j] = 1
    
    # 상하좌우를 나타냄
    # Up, Down, Left, Right
    dx = [0, 0, -1, 1]   # 각 방향에 대한 x좌표 변화 
    dy = [1, -1, 0, 0]   # 각 방향에 대한 y좌표 변화 
    
    # 큐에 캐릭터 출발지점 추가 & 최단거리를 적어줄 visited 배열 선언
    q = deque()
    q.append([characterX * 2, characterY * 2])   # 시작
    visited = [[1] * 102 for i in range(102)]  # 초기에 모든 좌표를 방문하지 않은 상태로 표시하기 위해 모든 요소를 1로 초기화
    
    while q:    # q가 비워질 때까지 계속 실행
        x, y = q.popleft()   # 먼저 들어간 좌표를 꺼내온다 (큐)
        # 도착한 곳이 아이템이 있는 장소라면 현재의 최단거리(나누기 2)를 answer로 하고 while문을 빠져나옴
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2  # start->end 까지의 경로 길이가 2배가 되게 되므로, 정답을 리턴할 때는 나누기 2를 해야함
            break
        # 아니라면 상하좌우 네 방향을 체크하면서
        for k in range(4):
            nx = x + dx[k]   # nx = 다음 x좌표
            ny = y + dy[k]   # ny = 다음 y좌표
            # 현재 좌표가 테두리이고 아직 방문하지 않은 곳이라면 q에 추가 후 visited 최단거리로 갱신
            if field[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1   
                # print(visited) -------------- 2
                #  현재 좌표의 최단거리 값에 1을 더하여 다음 좌표의 최단거리 값을 업데이트 -------------- 2
    
    return answer