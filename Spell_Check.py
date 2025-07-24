def spellCheck(s, n):
    if n != 5:
        return False
    return "".join(sorted(s)) == "Timru"


for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    print("YES" if spellCheck(s, n) else "NO")
