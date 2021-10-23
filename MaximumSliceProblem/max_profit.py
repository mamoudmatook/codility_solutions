# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if not A:
        return 0
    max_profit = 0
    current_stock = A[0]
    for i in A:
        if i > current_stock:
            if i - current_stock > max_profit:
                max_profit = i - current_stock
        else:
            current_stock = i
    return max_profit
