# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    min_idx = 0
    min_avg = (A[0] + A[1]) / 2
    current_avg = 0
    for i in range(0, len(A) - 2):
        current_avg = (A[i] + A[i + 1]) / 2
        if current_avg < min_avg:
            min_avg = current_avg
            min_idx = i
        current_avg = (A[i] + A[i + 1] + A[i + 2]) / 3
        if current_avg < min_avg:
            min_avg = current_avg
            min_idx = i

    current_avg = (A[-2] + A[-1]) / 2
    if current_avg < min_avg:
            min_idx = len(A) - 2

    return min_idx

solution([4, 2, 2, 5, 1, 5, 8])