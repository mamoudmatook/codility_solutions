# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    stack = []
    blocks = 0
    for i in range(len(H)):
        while stack and stack[-1] > H[i]:
            stack.pop()
        if stack and stack[-1] == H[i]:
            continue
        else:
            stack.append(H[i])
            blocks += 1
    return blocks
