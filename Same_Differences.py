from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    diff = defaultdict(int)
    for i in range(n):
        diff[a[i] - i] += 1
    res = 0
    for val in diff.values():
        res += val * (val - 1) // 2
    print(res)
