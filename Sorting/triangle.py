# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N = len(A)
    if N < 3:
        return 0
    A.sort():
    for i in range(N - 2):
        if A[i] + A[i + 1] <  A[i + 2]:
            return 1
    return 0
