# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")



def solution(A):
    N = len(A)
    prefix_sum = [0] * N
    prefix_sum[0] = A[0]
    passing_cars = 0
    for i in range(1, N):
        prefix_sum[i] = prefix_sum[i - 1] + A[i]
    for i in range(N):
        if A[i] == 1:
            continue
        passing_cars += prefix_sum[-1] - prefix_sum[i]

    return passing_cars if passing_cars <= 1000000000 else -1
