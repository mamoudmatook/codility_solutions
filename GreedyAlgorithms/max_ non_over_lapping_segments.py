# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    end = -1
    count = 0
    for i in range(len(A)):
        if A[i] > end:
            count += 1
            end = B[i]
    return count
