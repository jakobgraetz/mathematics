// main.swift
// author Jakob Grätz (@jakobgraetz)
// copyright 2024 - Jakob Grätz (@jakobgraetz)
// version 19/03/2024 (DD/MM/YYYY)
// description Implementation of my maths repository in Swift.

// Exception for Handling Division by Zero
enum DivisionError: Error {
    case divisionByZero
}

// Sum Function
func simple_sum (first_summand: Float64, second_summand: Float64) -> Float64 {
    return first_summand + second_summand
}

// Difference Function
func simple_difference (minuend: Float64, subtrahend: Float64) -> Float64 {
    return minuend - subtrahend
}

// Product Function
func simple_product (first_factor: Float64, second_factor: Float64) -> Float64 {
    return first_factor * second_factor
}

// Division Function
func simple_quotient (numerator: Float64, denominator: Float64) throws -> Float64 {
    guard denominator != 0 else {
        throw DivisionError.divisionByZero
    }

    return numerator / denominator
}