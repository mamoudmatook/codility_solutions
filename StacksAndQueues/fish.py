# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
UPSTREAM = 0
DOWNSTREAM = 1


def solution(A, B):
    stack = []
    eaten = 0
    for direction, size in zip(B, A):
        if direction == UPSTREAM:
            while stack:
                if size < stack[-1]:
                    eaten += 1
                    break
                else:
                    eaten += 1
                    stack.pop()
        else:
            stack.append(size)

    return len(A) - eaten

solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0])
