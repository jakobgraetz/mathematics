# main.py
# author Jakob Grätz (@jakobgraetz)
# copyright 2024 - Jakob Grätz (@jakobgraetz)
# version 19/03/2024 (DD/MM/YYYY)
# description Implementation of my maths repository in Python.

# Exception for Handling Division by Zero
class DivisionByZeroError(Exception):
    pass

# Sum Function
def simple_sum(first_summand: float, second_summand: float) -> float:
    return first_summand + second_summand

# Difference Function
def simple_difference(minuend: float, subtrahend: float) -> float:
    return minuend - subtrahend

# Product Function
def simple_product(first_factor: float, second_factor: float) -> float:
    return first_factor * second_factor

# Division Function
def simple_quotient (numerator: float, denominator: float):
    if denominator != 0:
        return numerator / denominator
    else:
        raise DivisionByZeroError("Division by zero is not allowed")