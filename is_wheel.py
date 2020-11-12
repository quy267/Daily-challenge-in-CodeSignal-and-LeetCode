# https://app.codesignal.com/challenge/CZBN32YvXfKqwX9h6


def isWheel(adj):
    result = list()
    for x, _ in enumerate(adj):
        result.append(0)
        for y, _ in enumerate(adj):
            if adj[x][y] and x == y:
                return False
            if adj[x][y]:
                result[x] += 1
    count3 = 0
    count_length = 0
    for _, item in enumerate(result):
        if item == 3:
            count3 += 1
        elif item == len(adj) - 1:
            count_length += 1
    if (count3 == len(adj) - 1 and count_length == 1) or (count3 == len(adj) and len(adj) == 4):
        return True

    return False


if __name__ == '__main__':
    print(isWheel(
        adj=[[False, True, True, True, True],
             [True, False, True, False, True],
             [True, True, False, True, False],q
             [True, False, True, False, True],
             [True, True, False, True, False]])
    )
