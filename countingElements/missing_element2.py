# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N = len(A)
    result = 0
    for e in A:
        if e > 0:
            result |= (1 << (e - 1))

    for i in range(N + 2):
        if not result & (1 << i):
            return i + 1

    
    
print(solution([-1, 1, 2, 3]))