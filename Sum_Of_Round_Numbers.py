t = int(input())
for _ in range(t):
    n = int(input())
    s = str(n)
    l = list(s)
    a = len(l)
    zero = l.count("0")
    print(a - zero)
    for i in range(a):
        if l[i] > "0":
            b = int(l[i])
            c = a - 1 - i
            print(b * 10**c, end=" ")
    print()
