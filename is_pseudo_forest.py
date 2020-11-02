# https://app.codesignal.com/challenge/yT5pFLMH8zZNh3BN7

def isPseudoforest(n, wmap):
    l = [[] for _ in range(n)]
    for i, j in wmap:
        l[i] += j,
        l[j] += i,

    print(l)
    f = 1
    while f:
        f = 0
        for i in range(n):
            if len(l[i]) == 1:
                j = l[i].pop()
                l[j].remove(i)
                f = 1
    print(l)
    return max(map(len, l)) < 3


if __name__ == '__main__':
    print(isPseudoforest(7, [[0, 1], [1, 2], [2, 3], [3, 1], [3, 4], [5, 6]]))
