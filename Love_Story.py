for _ in range(int(input())):
    s = input()
    print(sum(1 for i in range(10) if s[i] != "codeforces"[i]))
