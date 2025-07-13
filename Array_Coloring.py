for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print("NO" if sum(a) % 2 else "YES")
