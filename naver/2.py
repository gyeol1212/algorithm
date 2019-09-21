test = [
    "######",
    ">#*###",
    "####*#",
    "#<#>>#",
    ">#*#*<",
    "######"
]
l = len(test)
res = []
for i in range(6):
    success = False
    x, y = 0, i
    cnt = 0
    while x != l-1:
        if test[x][y] == "#":
            x += 1
        elif test[x][y] == ">":
            y += 1
        elif test[x][y] == "<":
            y -= 1
        else:
            if cnt == 1:
                break
            else:
                x += 1
                cnt += 1
    if x == l-1:
        res.append(i)

print(res)
