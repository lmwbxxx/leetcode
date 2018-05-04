# -*- coding: utf-8 -*-
"""
Created on Thu May  3 23:50:28 2018

@author: wx
"""

import random, math, numbers
from itertools import permutations, product

oper = {'+', '-', '*', '/'}
# oper = {'+', '-', '*', '/', 'p', 'r', 'l'}


def rpn(exp):  # calculating value from expressions
    stack = []
    for i in exp:
        if i in oper:
            num_right = stack.pop()
            num_left = stack.pop()
            result = cal(num_left, num_right, i)
            if result is False: return None
            stack.append(result)
        else:
            stack.append(i)
    assert len(stack) == 1
    return stack[0]


def cal(left, right, op):
    if op == '+':
        return left + right
    if op == '-':
        return left - right
    if op == '*':
        return left * right
    if op == '/':
        if right == 0:  # division by zero
            return False
        return left / right
    """
    if op == 'p':
        return left ** right
    if op == 'r':
        if right == 0:
            return False
        return left ** (1 / right)
    if op == 'l':
        if right <=0 or left<=0: return False
        return math.log(right, left)
    """


def is_valid(rpn_exp):  # check if the expression is valid
    d = 0
    o = 0
    for i in rpn_exp:
        if str.isdigit(str(i)):
            d += 1
        else:
            o += 1
        if d - o < 1:
            return False
    return True


def generate_exp(l):
    solution = []
    oper_exp_list = product(oper, repeat=3)  # choose 3 operators
    for oper_exp in oper_exp_list:
        s = l + list(oper_exp)  # using Reverse Polish Notation
        rpn_exp_list = set(permutations(s))  # permutation of digits and operators
        for rpn_exp in rpn_exp_list:
            if is_valid(rpn_exp):
                if rpn(rpn_exp) is not None:
                    value = rpn(rpn_exp)
                    if isinstance(value, numbers.Real) and \
                    math.isclose(24, value):
                        solution.append(rpn_exp)
    return solution


def main():
    l = [random.randint(1, 10) for i in range(4)]  # generate random numbers
    print("The chosen integers are:", *l)
    solution = list(set(generate_exp(l)))
    if len(solution) == 0:
        print("No solution")
    else:
        for i in solution:
            print(*i)


main()