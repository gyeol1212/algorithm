a = list(input())
b = list(input())
x = []
y = []
r = []


def rev(x):
    arr = []
    while len(x):
        arr.append(x.pop())
    return arr


x, y = rev(a), rev(b)

l = 0
lx = len(x)
ly = len(y)
minus = False
if lx < ly:
    x, y = y, x
    lx, ly = ly, lx
    minus = True
elif lx == ly:
    for i in range(lx):
        if x[i] > y[i]:
            break
        elif x[i] < y[i]:
            x, y = y, x
            lx, ly = ly, lx
            minus = True
            break


up = 0
for i in range(lx):
    if i < lx and i < ly:
        a = int(x[i])
        b = int(y[i])
        if a - b + up < 0:
            r.append(a-b+up+10)
            up = -1
        else:
            r.append(a-b+up)
            up = 0
    elif i < lx:
        a = int(x[i])
        print(a, up)
        if a + up < 0:
            r.append(a+up+10)
            up = -1
        else:
            r.append(a+up)
            up = 0

print(r)
while r[len(r)-1] == 0 and len(r) != 1:
    r.pop()
if minus:
    print('-', end="")
for i in rev(r):
    print(i, end="")
