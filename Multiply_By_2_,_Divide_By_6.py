for _ in range(int(input())):
    n = int(input())
    cnt = 0
    while n != 1:
        if n % 6 == 0:
            n //= 6
            cnt += 1
        elif n % 3 == 0:
            n *= 2
            cnt += 1
        else:
            cnt = -1
            break
    print(cnt)
