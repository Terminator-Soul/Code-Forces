for _ in range(int(input())):
    n = int(input())
    s = input()
    left, right = 0, len(s) - 1
    while left < right and s[left] != s[right]:
        left += 1
        right -= 1
    print(right - left + 1)
