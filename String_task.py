string = input().lower()
s = []
new = ""
for i in string:
    if i in "AOYEUIaoyeui":
        continue
    else:
        s.append("." + i)
for i in s:
    new += i
print(new)
