# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from os import system


def solution(S):
    # write your code in Python 3.6
    open_bracktes = '({['
    BRACKETS = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for s in S:
        if s in open_bracktes:
            stack.append(s)
        else:
            if not stack:
                return 0
            symbol = stack[-1]
            if BRACKETS[symbol] != s:
                return False
            stack.pop()
    return not stack
        
            
    
    
