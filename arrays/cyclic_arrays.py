# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A, K):
    # write your code in Python 3.6
    if len(A) == 0:
        return A
    K = K % len(A)

    def rotate_one():

        tmp = A[-1]
        for i in range(len(A) - 1, 0, -1):
            A[i] = A[i - 1]
        A[0] = tmp

    for i in range(K):
        rotate_one()
    return A


solution([3, 8, 9, 7, 6], 3)
