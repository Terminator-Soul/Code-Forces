import bisect

n = int(input())

a = list(map(int, input().split()))

a.sort()

m = int(input())

for _ in range(m):
    k = int(input())
    ans = bisect.bisect_right(a, k)
    print(ans)
