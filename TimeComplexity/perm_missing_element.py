# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N = len(A)
    result = 0
    for i, v in enumerate(A):
        result ^= v
        result ^= (i + 1)
    
    return result ^ (N + 1)

