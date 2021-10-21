# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    count = 0
    for i in range(X, Y, D):
        count += 1
    return count
