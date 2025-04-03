word = input().split()
out = ""
for i in range(len(word)):
    temp = word[i]
    word[i] = temp[0].upper() + temp[1:]
    out += word[i]
print(out)
