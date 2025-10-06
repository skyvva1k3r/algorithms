import sys


def main():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    dist = [[10**9] * m for _ in range(n)]
    dist[0][0] = matrix[0][0]

    for i in range(n):
        for j in range(m):
            dist[i][j] = min(dist[i][j], dist[i - 1][j] + matrix[i][j],  dist[i][j - 1] + matrix[i][j])
    print(dist[n - 1][m - 1])

if __name__ == '__main__':
    main()
