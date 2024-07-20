from collections import deque

def solution(begin, target, words):
    answer = 0
    # begin에서 변환될 수 있는 단어도 파악해야하므로 추가
    words.append(begin)
    graph = [[] for _ in range(len(words))]
    visited = [0]*len(words)
    
    # 각 단어에 대해, 그 단어와 words의 다른 모든 단어들과
    # 비교하여 변환가능한 단어를 연결 그래프로 나타내기
    for i in range(len(words)):
        word = words[i] # 기준 단어
        for j in range(len(words)):
            compared = words[j] # 비교할 단어
            cnt = 0
            for c_idx in range(len(word)):
                if word[c_idx] != compared[c_idx]:
                    cnt += 1
            if cnt == 1: # 한 글자만 다르면 변환 가능이므로 간선 정보 추가
                graph[i].append(j)
    
    q = deque([len(words)-1])
    visited[len(words)-1] = 1 # 출발 노드 재방문 방지를 위해 1 저장
    
    while q:
        word_num = q.popleft()
        
        if words[word_num] == target:
            # 출발 노드 visited가 1이었으므로, 1을 빼준 값이 답임
            answer = visited[word_num] - 1
            break
        
        for adj_word_num in graph[word_num]:
            if visited[adj_word_num] == 0:
                visited[adj_word_num] = visited[word_num] + 1
                q.append(adj_word_num)
    
    return answer