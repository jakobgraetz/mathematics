package java;

// main.java
// author Jakob Grätz (@jakobgraetz)
// copyright 2024 - Jakob Grätz (@jakobgraetz)
// version 22/03/2024 (DD/MM/YYYY)
// description Implementation of my maths repository in Java.

// Exception for Handling Division by Zero
class DivisionByZeroException extends Exception {
    public DivisionByZeroException(String message) {
        super(message);
    }
}

public class main {
    // Main Method
    public static void main (String[] Args) {
        
    }

    // Sum Method
    public static Double simple_sum (Double first_summand, Double second_summand) {
        return first_summand + second_summand;
    }

    // Difference Method
    public static Double simple_difference (Double minuend, Double subtrahend) {
        return minuend - subtrahend;
    }

    // Product Method
    public static Double simple_product (Double first_factor, Double second_factor) {
        return first_factor * second_factor;
    }
    
    // Division Method
    public static Double simple_quotient (Double numerator, Double denominator) throws DivisionByZeroException {
        if (denominator != 0.0) {
            return numerator / denominator;
        } else {
            throw new DivisionByZeroException("Division by zero is not allowed");
        }
    }
}