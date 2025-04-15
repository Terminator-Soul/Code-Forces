def solution(coins):
    group1, group2, result_group, coins = 0, 0, 0, sorted(coins)
    for i in coins:
        group1 += i
    for i in coins[::-1]:
        group2 += i
        result_group += 1
        if group2 > (group1 / 2):
            break
    return result_group
coins = input()
print(solution(list(map(int, input().split()))))
