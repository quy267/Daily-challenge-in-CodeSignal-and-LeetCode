import re


def normalize(arr):
    result = list()
    for i, element in enumerate(arr):
        result.append(' '.join(set(re.sub(r'[^a-z\s]', "", element.lower()).split())))

    return result


def intersection(a, b):
    return list(set(a) & set(b))


def union(a, b):
    return list(set(a) | set(b))


def index_of_inter_section(needle, stack):
    for i, e in enumerate(stack):
        if len(intersection(e, needle)) > 0:
            return i
    return -1


def jac_card(a, b):
    if a is None or b is None or len(a) == 0 or len(b) == 0:
        return 0
    _intersection = len(intersection(a.split(), b.split()))
    _union = len(union(a.split(), b.split()))
    if _union == 0:
        return 0
    return _intersection / _union


def spamClusterization(requests, ids, threshold):
    if len(requests) != len(ids):
        return []

    r = normalize(requests)
    sets = list()
    for i, r_i in enumerate(r):
        aux = list()
        for j in range(i + 1, len(r)):
            if jac_card(r_i, r[j]) >= threshold:
                aux.append(ids[j])
        if len(aux) > 0:
            aux.append(ids[i])
            index = index_of_inter_section(aux, sets)
            if index >= 0:
                aux = union(sets[index], aux)
            else:
                index = len(sets) - 1
            if index >= 0:
                sets[index] = tuple(sorted(aux))

    sorted(sets)

    return sorted(sets, key=lambda a: a[0])


if __name__ == '__main__':
    spamClusterization(requests=["I need a new window.",
                                 "I really, really want to replace my window!",
                                 "Replace my window.",
                                 "I want a new window.",
                                 "I want a new carpet, I want a new carpet, I want a new carpet.",
                                 "Replace my carpet"],
                       ids=[374, 2845, 83, 1848, 1837, 1500],
                       threshold=0.5)
