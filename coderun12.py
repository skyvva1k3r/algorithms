import sys
from collections import deque

def main():
    n = int(input())
    temp = [list(map(int, input().split())) for _ in range(n)]
    graph = dict()
    for i in range(n):
        for j in range(n):
            if temp[i][j] == 1:
                if i not in graph:
                    graph[i] = set()
                graph[i].add(j)
    start, end = map(int, input().split())
    start, end = start - 1, end - 1
    visited = set([start])
    queue = deque([(start, 0)])
    while queue:
        node, distance = queue.popleft()
        if node == end:
            print(distance)
            return
        if node not in graph.keys():
            continue
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
    print(-1)


if __name__ == '__main__':
    main()
