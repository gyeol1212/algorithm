n = int(input())


def moun(a):
    if a == 1:
        print(1, end="")
    else:
        moun(a-1)
        print(a, end="")
        moun(a-1)


moun(n)
