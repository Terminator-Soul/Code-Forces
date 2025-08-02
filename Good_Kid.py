for _ in range(int(input())):
    int(input())
    a = list(map(int, input().split()))
    t = a.index(min(a))
    a[t] = a[t] + 1
    product = 1
    for num in a:
        product *= num
    print(product)
