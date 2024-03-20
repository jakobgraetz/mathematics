// main.rs
// author Jakob Grätz (@jakobgraetz)
// copyright 2024 - Jakob Grätz (@jakobgraetz)
// version 19/03/2024 (DD/MM/YYYY)
// description Implementation of my maths repository in Rust.

#[derive(Debug)]
enum DivisionError {
    DivisionByZero,
}

fn simple_sum (first_summand: f64, second_summand: f64) -> f64 {
    return first_summand + second_summand;
}

fn simple_difference (minuend: f64, subtrahend: f64) -> f64 {
    return minuend - subtrahend;
}

fn simple_product (first_factor: f64, second_factor: f64) -> f64 {
    return first_factor * second_factor;
}

fn simple_quotient (numerator: f64, denominator: f64) -> Result<f64, DivisionError> {
    if denominator != 0.0 {
        Ok(numerator / denominator)
    } else {
        Err(DivisionError::DivisionByZero)
    }
}

fn main () {
    
}