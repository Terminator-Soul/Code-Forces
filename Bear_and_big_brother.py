inp = input().split()
l, b, c = int(inp[0]), int(inp[1]), 0
while l <= b:
    l, b, c = 3 * l, 2 * b, c + 1
print(c)
