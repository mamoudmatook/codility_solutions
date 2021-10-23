# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N):
    squrt_of_n = int(N ** 0.5) + 1
    min_perm = 0
    current_perm = 0
    for i in range(1, squrt_of_n):
        if N % i == 0:
            current_perm = (i + N // i) * 2
            if current_perm < min_perm:
                min_perm = current_perm

    return current_perm
