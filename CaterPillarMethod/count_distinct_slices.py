# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(M, A):
    hash = [0] * (M + 1)
    slices = 0
    max_slices = 1000000000
    head = 0
    for tail in range(len(A)):
        while head < len(A) and ( not hash[A[head]]):
            hash[A[head]] = 1
            slices += head - tail + 1
            if slices > max_slices:
                return max_slices
            head += 1
        hash[A[tail]] = False
    return slices

solution(6, [3, 4, 5, 5, 2])
            
            

