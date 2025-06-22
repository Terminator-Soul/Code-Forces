def max_points(n, a):
    max_value = max(a)
    freq = [0] * (max_value + 1)
    for num in a:
        freq[num] += 1
    dp = [0] * (max_value + 1)
    dp[1] = freq[1]
    for i in range(2, max_value + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + i * freq[i])
    return dp[max_value]


n = int(input())
a = list(map(int, input().split()))
print(max_points(n, a))
