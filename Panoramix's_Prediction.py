n, m = map(int, input().split())
p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
print("YES" if m in p and p.index(m) - p.index(n) == 1 else "NO")
