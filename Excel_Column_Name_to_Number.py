def titleToNumber(title):
    if len(title) == 1:
        return ord(title) - ord('A') + 1
    powd, add = 1, 0
    for k in title[::-1]:
        add += powd * (ord(k) - ord('A') + 1)
        powd *= 26
    return add

title = input("Enter Column Title:- ")
print(titleToNumber(title))
