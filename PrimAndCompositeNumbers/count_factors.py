# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    if N == 1:
        return 1
    factors = 0
    for i in range(2, (N // 2) + 1):
        if N % i == 0:
            factors += 1
    return factors + 2

solution(24)