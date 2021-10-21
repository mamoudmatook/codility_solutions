# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    N = len(A)
    l_sum = A[0]
    r_sum = sum(A) - l_sum
    diff = abs(l_sum - r_sum)
    for i in range(1, N -1):
        l_sum += A[i]
        r_sum -= A[i]
        c_diff = abs(l_sum - r_sum)
        if diff > c_diff:
            diff = c_diff
    return diff
