n = int(input())
win = 0
for i in range(n):
    l_or_0 = input()
    if l_or_0.count("1") > 1:
        win += 1
print(win)
