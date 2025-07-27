for _ in range(int(input())):
    n = input().strip()
    length = len(n)
    print(((length * (length + 1)) // 2) + (10 * (int(n[0]) - 1)))
