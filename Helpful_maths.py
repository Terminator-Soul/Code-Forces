inp = input()
arr = []
for i in inp:
    if i.isdigit():
        arr.append(i)
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key
out = ""
for i in arr:
    out += i + "+"
print(out[: len(out) - 1])
