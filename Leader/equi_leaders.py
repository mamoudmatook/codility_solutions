# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def get_leader(A):
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

    return (leader, A.count(leader)) if int(A.count(leader) > len(A) / 2) else (-1, -1)


def solution(A):
    leader, leader_count = get_leader(A)
    if leader == -1:
        return 0

    left_leader_count = 0
    right_leader_count = leader_count
    left_count = 0
    right_count = len(A)
    equi_leaders = 0
    for i in A:
        if i == leader:
            left_leader_count += 1
            right_leader_count -= 1

        left_count += 1
        right_count -= 1

        if left_leader_count > left_count / 2 and right_leader_count > right_count / 2:
            equi_leaders += 1
    
    return equi_leaders
