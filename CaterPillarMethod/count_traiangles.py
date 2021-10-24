# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    A.sort()
    N = len(A)
    result  = 0
    for x in range(N - 2):
        z = x + 2
        for y in range(x + 1, N - 1):
            while z < N and (A[x] + A[y] > A[z]):
                z += 1
            result += z - y - 1

    return result

a = solution([10, 2, 5, 1, 8, 12])
print()
