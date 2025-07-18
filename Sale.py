n, m = list(map(int, input().rstrip().split()))
a = list(map(int, input().rstrip().split()))
a.sort()
total = 0
for i in a:
    if i < 0 and m > 0:
        total += i
        m -= 1
    if m == 0:
        break
print(-1 * total)
