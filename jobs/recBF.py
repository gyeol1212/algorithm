n = int(input())

res = []
for _ in range(n):
    res.append(0)


def getResult(current, num, arr):
    if current >= num:
        for a in arr:
            print(a, end="")
        print('')
    else:
        for i in range(1, n+1):
            if i not in arr:
                arr[current] = i
                getResult(current+1, num, arr)
                arr[current] = 0


getResult(0, n, res)
