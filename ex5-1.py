# 예제 5-1
"""
    0
  7/ \5
 1    2

위 같이 0, 1, 2를 노드로 갖고 가중치가 7, 5인 그래프를 구현하라
"""
graph = [[] for i in range(3)] # 노드 세개 생성

graph[0].append((1, 7))
graph[0].append((2, 5))
graph[1].append((0, 7))
graph[2].append((0, 5))

print(graph)
