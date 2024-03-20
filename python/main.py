# main.py
# author Jakob Grätz (@jakobgraetz)
# copyright 2024 - Jakob Grätz (@jakobgraetz)
# version 19/03/2024 (DD/MM/YYYY)
# description Implementation of my maths repository in Python.

class DivisionByZeroError(Exception):
    pass

def simple_sum(first_summand: float, second_summand: float):
    return first_summand + second_summand

def simple_difference(minuend: float, subtrahend: float):
    return minuend - subtrahend

def simple_product(first_factor: float, second_factor: float):
    return first_factor * second_factor

def simple_quotient (numerator: float, denominator: float):
    if denominator != 0:
        return numerator / denominator
    else:
        raise DivisionByZeroError("Division by zero is not allowed")