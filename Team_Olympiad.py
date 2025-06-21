n = int(input())
l = list(map(int, input().strip().split()))
a = 0
b = 0
c = 0
one = []
two = []
three = []
for i in range(n):
    if l[i] == 1:
        one.append(i + 1)
        a = a + 1
    elif l[i] == 2:
        two.append(i + 1)
        b = b + 1
    else:
        three.append(i + 1)
        c = c + 1
print(min(a, b, c))
for i in range(min(a, b, c)):
    print(one[i], end=" ")
    print(two[i], end=" ")
    print(three[i], end=" ")
    print()
