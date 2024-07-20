from collections import deque, defaultdict

# 4 방향 인접 노드로 이동
def adj_pos(x, y):
    yield x-1, y
    yield x+1, y
    yield x, y-1
    yield x, y+1

# (x, y)가 포함된 퍼즐 조각을 여백을 포함한 직사각형
# 형태로 나타낸 2차원 리스트와 조각의 1x1 칸 개수 합을 리턴
def make_puzzle_frag_and_sum(x, y, table, visited):
    # find puzzle location
    visited[x][y] = 1
    dq = deque([(x, y)])
    
    locations = []
    
    while dq:
        now_x, now_y = dq.popleft()
        locations.append((now_x, now_y))
        
        for adj_x, adj_y in adj_pos(now_x, now_y):
            if not (0 <= adj_x < len(table) and 0 <= adj_y < len(table[0])):
                continue
            
            if table[adj_x][adj_y] and not visited[adj_x][adj_y]:
                visited[adj_x][adj_y] = 1
                dq.append((adj_x, adj_y))
    
    # make puzzle frag
    r_all = [pos[0] for pos in locations]
    c_all = [pos[1] for pos in locations]
    
    r_min = min(r_all)
    r_max = max(r_all)
    c_min = min(c_all)
    c_max = max(c_all)
    
    r_len = r_max - r_min + 1
    c_len = c_max - c_min + 1
    
    frag = [[0]*c_len for _ in range(r_len)]
    
    for r in range(r_len):
        for c in range(c_len):
            frag[r][c] += table[r+r_min][c+c_min]
    
    return frag, len(locations)

def rotate(frag):
    r_len = len(frag)
    c_len = len(frag[0])
    
    frag_new = [[0]*r_len for _ in range(c_len)]
    
    for r in range(r_len):
        for c in range(c_len):
            frag_new[c][r_len-r-1] = frag[r][c]
    
    return frag_new

# 퍼즐 조각이 딱 들어맞는지 확인
# 퍼즐을 보드의 찾아낸 여백 뭉탱이의 개수에 딱 맞는
# 것을 대상으로 is_match를 실행하는 것이기 때문에,
# 퍼즐이 빈 칸에 딱 들어맞는 경우는, 아까 보드에서 찾은
# 직사각형 형태에서 모든 값이 1이 되는 경우말고는 없음.
def is_match(x, y, puzzle, game_board):
    for r in range(len(puzzle)):
        for c in range(len(puzzle[0])):
            if game_board[r+x][c+y] + puzzle[r][c] != 1:
                return False
    
    return True
    
def match_puzzle(r, c, frag_dict, visited_board, game_board):
    # check empty sum
    dq = deque([(r, c)])
    cnt = 0
    path = [(r, c)]
    
    while dq:
        now_x, now_y = dq.popleft()
        cnt += 1
        path.append((now_x, now_y))
        
        for adj_x, adj_y in adj_pos(now_x, now_y):
            if not(0 <= adj_x < len(game_board) and 0 <= adj_y < len(game_board[0])):
                continue
            
            if not game_board[adj_x][adj_y] and not visited_board[adj_x][adj_y]:
                visited_board[adj_x][adj_y] = 1
                dq.append((adj_x, adj_y))
    
    # 빈 공간의 칸 개수 체크한 뒤,
    # 그 칸 개수만큼에 해당하는 퍼즐 조각들을 대상으로
    # 딱 들어맞는지 is_match로 체크
    # game_board에서 탐색한 빈 칸 형태를 여백을 포함한 직사각형
    # 형태로 생각해봤을 때, 그 때의 왼쪽 맨 위에서 시작하여(r_min, c_min)
    # 퍼즐 조각(직사각형 형태)과 비교
    puzzles = frag_dict[cnt]
    r_min = min([pos[0] for pos in path])
    c_min = min([pos[1] for pos in path])
    
    for i in range(len(puzzles)):
        puzzle = puzzles[i]
        for _ in range(4):
            puzzle = rotate(puzzle)
            
            r_len = len(puzzle)
            c_len = len(puzzle[0])
            
            # 회전한 조각이 board 범위 안 넘어가는지 체크
            if not(0 <= r_min + r_len - 1 < len(game_board) and 0 <= c_min + c_len - 1 < len(game_board[0])):
                continue
            
            if is_match(r_min, c_min, puzzle, game_board):
                del frag_dict[cnt][i] # 사용한 조각 제거
                return cnt
    
    return 0
            

def solution(game_board, table):
    answer = 0
    
    # 퍼즐 조각 모두 찾기
    visited = [[0]*len(table) for _ in range(len(table[0]))]
    frag_dict = defaultdict(list)
    
    for r in range(len(table)):
        for c in range(len(table[0])):
            if table[r][c] and not visited[r][c]:
                frag, frag_sum = make_puzzle_frag_and_sum(r, c, table, visited)
                frag_dict[frag_sum].append(frag)
    
    # 보드에 조각 끼워넣기
    visited_board = [[0]*len(game_board) for _ in range(len(game_board[0]))]
    for r in range(len(game_board)):
        for c in range(len(game_board[0])):
            if not game_board[r][c] and not visited_board[r][c]:
                visited_board[r][c] = 1
                answer += match_puzzle(r, c, frag_dict, visited_board, game_board)
                
    return answer