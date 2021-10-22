# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


from math import floor, ceil


def solution(A, B, K):
    start  = ceil(A / K)
    end = floor(B / K)
    return end - start + 1


solution(11, 345, 17)
