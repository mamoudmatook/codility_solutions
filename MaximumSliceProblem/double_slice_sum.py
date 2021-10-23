# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    N = len(A)
    if N == 3:
        return 0
    prefixes = [0] * N
    suffixes = [0] * N
    for i in range(1, N - 1):
        prefixes[i] = max(A[i], prefixes[i - 1] + A[i])
        if prefixes[i] < 0:
            prefixes[i] = 0
        suffixes[N - 1 - i] = max(A[N - 1 - i], suffixes[N - 1 - i + 1] + A[N - 1 - i])
        if suffixes[N - 1 - i] < 0:
            suffixes[N - 1 - i] = 0
    max_double = 0
    for i in range(1, N - 1):
        max_double = max(prefixes[i - 1] + suffixes[i + 1], max_double)
    return max_double


a = solution([0, 10, -5, -2, 0])
print()
