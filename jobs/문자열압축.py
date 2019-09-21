string = input()
r = ''
t = ''
cnt = 1
for i in string:
    if t == i:
        cnt += 1
    else:
        if cnt > 1:
            r += str(cnt)
            cnt = 1
        r += t
        t = i
if cnt > 1:
    r += str(cnt)
r += t
print(r)
