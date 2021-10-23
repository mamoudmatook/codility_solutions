# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
OPEN = "("


def solution(S):
    # write your code in Python 3.6
    stack = []
    for s in S:
        if s == OPEN:
            stack.append()
        else:
            if not stack:
                return 0
            else:
                stack.pop()

    return int(stack)
