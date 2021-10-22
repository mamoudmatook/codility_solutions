# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    hash_set = set()
    for e in A:
        hash_set.add(e)
    for i in range(1, len(A) + 2):
        if i not in hash_set:
            return i
          
