for _ in range(int(input())):
    a, b = list(map(str, input().split()))
    print(b[0] + a[1:], a[0] + b[1:])
