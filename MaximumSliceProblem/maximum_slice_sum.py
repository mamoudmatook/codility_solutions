# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    sum = - float('inf')
    max_sum = - float('inf')
    for i in A:
        sum = max(sum + i, i)
        max_sum = max(max_sum, sum)

    return max_sum
