# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    hash = set()
    for e in A:
        hash.add(abs(e))
    return len(hash)
