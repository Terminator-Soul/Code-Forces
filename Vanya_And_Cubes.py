a = int(input())
c, i, l = 0, 0, 0
while c <= a:
    i += 1
    l += i
    c = c + l
print(i - 1)
