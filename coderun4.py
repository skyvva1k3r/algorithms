import sys
from collections import deque


def main():
    n, m = map(int, input().split())
    dist = {(0,0): 1}

    for i in range(0, n):
        for j in range(0, m):
            if (i,j) in dist:
                if (i + 2 < n and j + 1 < m):
                    dist[(i+2, j+1)] = dist.get((i+2, j+1), 0) + dist[(i,j)]
                if (i + 1 < n and j + 2 < m):
                    dist[(i+1, j+2)] = dist.get((i+1, j+2), 0) + dist[(i,j)]
    try:
        print(dist[n-1, m-1])
    except KeyError:
        print(0)
    if n == 1 and m == 1:
        print(0)

if __name__ == '__main__':
    main()