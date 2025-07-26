n, t = map(int, input().split())
jumps = list(map(int, input().split()))
i = 0
while i < t - 1:
    i += jumps[i]
print("YES" if i == t - 1 else "NO")
