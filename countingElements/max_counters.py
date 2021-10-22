# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(N, A):
    last_update_to_max = 0
    current_max = 0

    result = [0] * N
    for i, v in enumerate(A):
        if v > N:
            last_update_to_max = current_max
        else:
            if result[v - 1] < last_update_to_max:
                result[v - 1] = last_update_to_max + 1
            else:
                result[v - 1] += 1

            if result[v - 1] > current_max:
                current_max = result[v - 1]

    for i in range(len(result)):
        if result[i] < last_update_to_max:
            result[i] = last_update_to_max

    return result


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))