s = input("Enter a string of characters: ")
sa = []
i = 0
c = 0

while i < len(s):
    while s[i] == s[i + 1]:
        c += 1
        i += 1
        if i + 1 >= len(s):
            break
    sa.append(s[i])
    c += 1
    sa.append(c)
    c = 0
    i += 1

print("".join(map(str, sa)))

# ==============================================

s = input("Enter a string of characters: ")
sa = str()
i = 0

while i < len(s):
    sa += s[i]
    j = 0
    while j < int(s[i + 1]) - 1:
        sa += s[i]
        j += 1
    i += 2

print(sa)
