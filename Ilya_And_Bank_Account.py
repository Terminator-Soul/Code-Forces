n = int(input())
print(max(n, int(str(n)[:-1]), int(str(n)[:-2] + str(n)[-1])))
