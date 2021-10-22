# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S, P, Q):
    N = len(S)
    A_prefix_sums = [0] * (N + 1)
    C_prefix_sums = [0] * (N + 1)
    G_prefix_sums = [0] * (N + 1)
    factors = {"A": 1, "C": 2, "G": 3, "T": 4}
    for i in range(N):
        a, c, g = 0, 0, 0
        if S[i] == "A":
            a = 1
        elif S[i] == "C":
            c = 1
        elif S[i] == "G":
            g = 1

        A_prefix_sums[i + 1] = A_prefix_sums[i] + a
        C_prefix_sums[i + 1] = C_prefix_sums[i] + c
        G_prefix_sums[i + 1] = G_prefix_sums[i] + g

    result = []
    for i in range(len(P)):
        if S[P[i]] == "A" or A_prefix_sums[Q[i] + 1] - A_prefix_sums[P[i] + 1] > 0:
            result.append(factors["A"])
        elif S[P[i]] == "C" or C_prefix_sums[Q[i] + 1] - C_prefix_sums[P[i] + 1] > 0:
            result.append(factors["C"])
        elif S[P[i]] == "G" or G_prefix_sums[Q[i] + 1] - G_prefix_sums[P[i] + 1] > 0:
            result.append(factors["G"])
        else:
            result.append(factors["T"])

    return result


S = "CAGCCTA"
P = [2, 5, 0]
Q = [0, 1, 2]
solution(S, P, Q)
