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
if lx > ly:
    l = lx
else:
    l = ly

up = 0
for i in range(l):
    if i < lx and i < ly:
        a = int(x[i])
        b = int(y[i])
        if a + b + up >= 10:
            r.append(a+b+up-10)
            up = 1
        else:
            r.append(a+b+up)
            up = 0
    elif i < lx:
        a = int(x[i])
        if a + up >= 10:
            r.append(a+up-10)
            up = 1
        else:
            r.append(a+up)
            up = 0
    elif i < ly:
        a = int(y[i])
        if a + up >= 10:
            r.append(a+up-10)
            up = 1
        else:
            r.append(a+up)
            up = 0
if up:
    r.append(1)

for i in rev(r):
    print(i, end="")
