for _ in range(int(input())):
    length, target = list(map(int, input().rstrip().split()))
    array = list(map(int, input().rstrip().split()))
    print("YES" if target in array else "NO")
