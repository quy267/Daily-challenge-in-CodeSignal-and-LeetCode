"""
https://app.codesignal.com/challenge/SFoZuf6cciFS8kpeD
"""


def make_tree(files, parents):
    tree = []
    for e, i in enumerate(files):
        index = e
        tree.append([i])
        while True:
            if parents[index] == "-1":
                tree[e].append("-1")
                break
            else:
                tree[e].append(parents[index])
                index = files.index(parents[index])
    print(tree)
    return tree


def find_closest(branch_1, branch_2):
    distances = []
    for f, i in enumerate(branch_1):
        for j, e in enumerate(branch_2):
            if e == i:
                distances.append([e, abs(j - f)])
    lowest = 10
    for i in distances:
        if i[1] < lowest:
            lowest = i[1]
            answer = i[0]
    return answer


def closest_common_parent(files, parents, file1, file2):
    tree = make_tree(files, parents)
    for i in tree:
        if i[0] == file1:
            branch_1 = i
        if i[0] == file2:
            branch_2 = i
    return find_closest(branch_1, branch_2)


if __name__ == '__main__':
    print(closest_common_parent(
        files=["F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"],
        parents=["-1", "F1", "F1", "F2", "F2", "F4", "F4", "F4"],
        file1="F5",
        file2="F8"
    ))
