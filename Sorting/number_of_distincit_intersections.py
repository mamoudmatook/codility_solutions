# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from bisect import bisect_right
def solution(A):
    intervals = sorted([(i - A[i], i + A[i]) for i in range(len(A))])
    starts = [e[0] for e in intervals]
    intersections = 0
    for i, val in enumerate(intervals):
        count = bisect_right(starts, val[1])
        count -= (i + 1)
        intersections += count
        if intersections > 10000000:
            return -1
    return intersections

