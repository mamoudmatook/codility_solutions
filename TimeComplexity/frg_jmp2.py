# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    distanc = Y - X
    if distanc % D == 0:
        return distanc // D
    else:
        return (distanc // D) + 1
        
