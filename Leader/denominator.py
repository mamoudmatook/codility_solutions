# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(A):
    # write your code in Python 3.6
    leader = 0
    leader_count = 0
    for i in A:
        if leader_count == 0:
            leader = i
            leader_count += 1
        elif i == leader:
            leader_count += 1
        else:
            leader_count -= 1

    return A.index(leader) if int(A.count(leader) > len(A) / 2) else -1
