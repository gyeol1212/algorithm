a = int(input())


def goBin(a):
    if a == 0:
        print(0, end="")
    elif a == 1:
        print(1, end="")
    else:
        goBin(a//2)
        print(a % 2, end="")


goBin(a)
