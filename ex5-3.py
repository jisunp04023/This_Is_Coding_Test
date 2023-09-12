# 예제 5-3
"""
DFS 예제
"""
def bfs(graph, start, visited):
    queue = [start] # 큐에 삽입
    visited[start] = True # 방문처리

    while len(queue):
        v = queue.pop(0)
        print(v, end = ' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

graph = [[],
         [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7]]

visited = [False] * 9

bfs(graph, 1, visited)
