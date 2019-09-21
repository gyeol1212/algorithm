arr = [[1, 0, 3], [2, 1, 3], [3, 3, 2], [4, 6, 2], [5, 7, 1]]
l = len(arr)
wait = []
wait_time = 0
current_time = 0
current = None
res = []
for i in range(l+1):
    if i == l:
        while len(wait):
            # 대기중 가장 작은 시간
            t = [0, 0, 999]
            for w in wait:
                if w[2] < t[2]:
                    t = w
            wait.remove(t)
            res.append(t[0])
        break
    # 인풋 시간 인지
    while arr[i][1] != current_time:
        current_time += 1
        # 대기 시간 지났으면
        if wait_time <= current_time and len(wait):
            # 대기중 가장 작은 시간
            t = [0, 0, 999]
            for w in wait:
                if w[2] < t[2]:
                    t = w
            wait.remove(t)
            wait_time = current_time + t[2]
            res.append(t[0])

    wait.append(arr[i])
    print(wait)

print(res)
