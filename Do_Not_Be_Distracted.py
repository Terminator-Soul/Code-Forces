for _ in range(int(input())):
    n = int(input())
    tasks = input()
    valid = True
    last_task = None
    seen_tasks = set()
    for i in range(n):
        if tasks[i] != last_task:
            if tasks[i] in seen_tasks:
                valid = False
                break
            seen_tasks.add(last_task) if last_task else None
            last_task = tasks[i]
    print("YES" if valid else "NO")
