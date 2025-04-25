n = int(input())
c = list(map(int, input().strip().split()))
e = max(c)
l = min(c)
e = c.index(e)
d = e
e = c.pop(e)
c = [e] + c
c = c[::-1]
l = c.index(l)
print(l + d)
