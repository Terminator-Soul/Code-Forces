for _ in range(int(input())):
    s = input()
    n = len(s)
    print("YES" if s[: n // 2] == s[n // 2 :] else "NO")
