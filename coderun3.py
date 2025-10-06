import sys


def main():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    dist = [[0] * m for _ in range(n)]
    path = [[[]] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
                dist[i][j] = max(dist[i][j], dist[i - 1][j] + matrix[i][j],  dist[i][j - 1] + matrix[i][j])
                if dist[i][j] == dist[i - 1][j] + matrix[i][j]:
                    path[i][j] = path[i - 1][j] + ["D"]
                else:
                    path[i][j] = path[i][j - 1] + ["R"]
    print(dist[n - 1][m - 1], "\n", " ".join(path[n - 1][m - 1][1::]), sep = "")

if __name__ == '__main__':
    main()
