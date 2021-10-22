# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N = len(A)
    ones = int('1' * N, 2)
    result = 0
    for i,v in enumerate(A):
        if result & (1 << (v -1)):
            return 0
        else:
            result |= (1 << (v - 1))

    return int(result == ones)
