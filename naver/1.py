n = int(input())
cnt = 0
for i in range(n):
    a = input()
    first_array = a.split('@')
    if len(first_array) == 2:
        second_array = first_array[1].split('.')
        if len(second_array) == 2:
            cnt += 1
            print(a)
print(cnt)
