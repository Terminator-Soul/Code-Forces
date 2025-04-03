s = input()
l, u = 0, 0
for i in s:
    if i.islower():
        l += 1
    elif i.isupper():
        u += 1
if l >= u:
    print(s.lower())
else:
    print(s.upper())
