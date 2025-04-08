from re import match
s = input()
if match(r'.*h.*e.*l.*l.*o.*', s):
    print('YES')
else:
    print('NO')