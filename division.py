def divide_numbers(a, b):
    """
    Divide two numbers and return the result.
    
    Args:
        a: Numerator (dividend)
        b: Denominator (divisor)
    
    Returns:
        The result of a divided by b
    
    Raises:
        ValueError: If b is zero (division by zero)
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    # Test the function
    result = divide_numbers(10, 2)
    print(f"10 / 2 = {result}")
    
    result = divide_numbers(15, 3)
    print(f"15 / 3 = {result}")
    
    result = divide_numbers(7, 2)
    print(f"7 / 2 = {result}")
    
    # Test error handling
    try:
        result = divide_numbers(10, 0)
        print(f"10 / 0 = {result}")
    except ValueError as e:
        print(f"Error: {e}")
