n = input()
n = input()
a, d = n.count("A"), n.count("D")
if a > d:
    print("Anton")
elif d > a:
    print("Danik")
elif d == a:
    print("Friendship")
