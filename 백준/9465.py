#botom-up 방법 사용!
import sys
input = sys.stdin.readline
n = int(input())

def sticker(value, dp, a):
    dp[0][0], dp[1][0], dp[2][0] = value[0][0], value[1][0], 0
    for i in range(1, a):
        dp[0][i] = max(dp[1][i-1], dp[2][i-1]) + value[0][i]
        dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + value[1][i]
        dp[2][i] = max(dp[0][i-1], dp[1][i-1])
    maxf = 0
    for i in range(2):
        if maxf <= dp[i][a-1]:
            maxf = dp[i][a-1]
    #maxf = max(dp[i][0], max(dp[i][1], dp[i][2])) 이렇게 표현 가능!!
    print(maxf)

for i in range(n):
    a = int(input())
    value = [0,0]
    dp = list([0]*a for i in range(3))
    memo = [0]*n
    for i in range(2):
        value[i] = list(map(int, input().split()))
    sticker(value, dp, a)















