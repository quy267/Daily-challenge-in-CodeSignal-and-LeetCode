import textwrap


def solution(feedback, size):
    return textwrap.wrap(feedback, size)


if __name__ == '__main__':
    print(solution("This is an example feedback", 8))
