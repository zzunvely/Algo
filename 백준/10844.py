import sys
input = sys.stdin.readline
n = int(input())
dp = [[0]*10 for i in range(n+1)]
for i in range(1, 10):
    dp[1][i] = 1
for i in range(2 , n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j==9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j+1]
final = 0
for i in range(10):
    final +=dp[n][i]
print(final%1000000000)
