def rev(x):
    arr = []
    while len(x):
        arr.append(x.pop())
    return arr


def plus(a, b):
    a = list(a)
    b = list(b)
    x = []
    y = []
    r = []

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
    res = ''
    for i in rev(r):
        res += str(i)
    return res


a = list(input())
b = list(input())
x = rev(a)
y = rev(b)
l = len(y)
r = '0'
for i in range(l):
    up = 0
    res = []
    for k in x:
        t = int(k) * int(y[i]) + up
        if t >= 10:
            res.append(t % 10)
            up = t//10
        else:
            res.append(t)
            up = 0
    if up:
        res.append(up)
    temp = ''
    for j in rev(res):
        temp += str(j)
    temp += '0' * i
    r = plus(r, temp)

print(r)
