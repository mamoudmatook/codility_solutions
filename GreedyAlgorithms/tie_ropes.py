# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(K, A):
    rop_len = 0
    count = 0
    for r in A:
        rop_len += r
        if rop_len >= K:
            count += 1
            rop_len = 0
    return rop_len

print(solution(4, [1, 2, 3, 4, 1, 1, 3]))
