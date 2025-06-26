import math


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


n = 7 - max(map(int, input().split()))
g = gcd(n, 6)
print(f"{n // g}/{6 // g}")
