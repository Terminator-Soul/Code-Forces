for i in range(int(input())):
    number_of_problems = int(input())
    map = []
    teams = input()
    count = 0
    for team in teams:
        if team not in map:
            map.append(team)
            count += 2
        else:
            count += 1
    print(count)
