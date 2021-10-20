# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, K):
    N = len(A)
    if N == 0:
        return A
    result = [0] * N
    K = K % N
    for i, v in enumerate(A):
        result[(i + K) % N] = v
    return result
