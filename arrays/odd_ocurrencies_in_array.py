# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    result = 0
    for a in A:
        result &= a
    return result

    
