n, k = map(int, input().split())


def rec(n, k, res, cnt, current):
    # print('******')
    # print(res, cnt, current)
    # print('******')
    if current > n:
        print(res)
        return

    # 무조건 0
    if cnt == k:
        while len(res) != n:
            res += '0'
        print(res)
    # 무조건 1
    elif n-current+1 == k-cnt:
        while len(res) != n:
            res += '1'
        print(res)
    else:
        rec(n, k, res+'1', cnt+1, current+1)
        rec(n, k, res+'0', cnt, current+1)


rec(n, k, '', 0, 1)
