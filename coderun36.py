def main():
    l, n = map(int, input().split())
    cuts = list(map(int, input().split()))
    cuts = [0] + sorted(cuts) + [l]

    dp = [[0] * (n + 2) for _ in range(n + 2)]

    for length in range(2, n + 2):
        for i in range(n + 2 - length):
            j = i + length
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                cost = cuts[j] - cuts[i] + dp[i][k] + dp[k][j]
                dp[i][j] = min(dp[i][j], cost)

    print(dp[0][n + 1])

if __name__ == '__main__':
    main()
