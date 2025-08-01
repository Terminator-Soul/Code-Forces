n, m = map(int, input().split())
operations = 0
while m > n:
    if m % 2 == 0:
        m //= 2
    else:
        m += 1
    operations += 1
operations += n - m
print(operations)
