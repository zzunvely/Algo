import sys
input = sys.stdin.readline
n = int(input())
dp = [0, 0, 0]
dp[0] = list(int(i) for i in input.strip().split())
dp[1] = [1]*n
for i in range(n):
    for j in range(i):
        if dp[0][j] < dp[0][i] and dp[1][i] < dp[1][j] + 1:
            dp[1][i] = dp[1][j] + 1
