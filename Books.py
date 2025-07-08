def solve():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    max_books = 0
    current_sum = 0
    left = 0

    for right in range(n):
        current_sum += a[right]
        while current_sum > t:
            current_sum -= a[left]
            left += 1
        max_books = max(max_books, right - left + 1)

    print(max_books)


solve()
