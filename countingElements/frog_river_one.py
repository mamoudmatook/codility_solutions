# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(X, A):
    ones = int("1" * X, 2)
    positions = 0
    for i, v in enumerate(A):
        positions |= (1 << (v - 1))
        if positions == ones:
            return i
    return -1

solution(5, [1, 3, 1, 4, 2, 3, 5, 4])