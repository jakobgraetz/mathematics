#include <iostream>
#include <stdexcept>

// main.cpp
// author Jakob Grätz (@jakobgraetz)
// copyright 2024 - Jakob Grätz (@jakobgraetz)
// version 19/03/2024 (DD/MM/YYYY)
// description Implementation of my maths repository in C++.

class DivisionByZeroException : public std::exception {
public:
    const char* what() const _NOEXCEPT override {
        return "Division by zero is not allowed";
    }
};

double simple_sum(double first_summand, double second_summand) {
    return first_summand + second_summand;
}

static double simple_difference(double minuend, double subtrahend) {
    return minuend - subtrahend;
}

static double simple_product(double first_factor, double second_factor) {
    return first_factor * second_factor;
}

static double simple_quotient(double numerator, double denominator) {
    if (denominator != 0) {
        return numerator / denominator;
    } else {
        throw DivisionByZeroException();
    }
}

int main () {
    return 0;
}