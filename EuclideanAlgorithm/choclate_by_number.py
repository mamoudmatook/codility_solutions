# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, M):
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a%b)
    
    return N // gcd(N, M)
    
