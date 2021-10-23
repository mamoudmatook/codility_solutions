# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    squrt_of_n = int(N ** 0.5) + 1
    factors = 0
    for i in range(1, squrt_of_n):
        if N % i == 0:
            if i != N ** 0.5:
                factors += 2
            else:
                factors += 1
    factors
    
