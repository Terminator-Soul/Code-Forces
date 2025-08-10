for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mn = min(a)
    ans = sum(x - mn for x in a)
    print(ans)
