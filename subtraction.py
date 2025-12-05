def subtract_numbers(a, b):
    """
    Subtract two numbers and return the result.
    
    Args:
        a: First number (minuend)
        b: Second number (subtrahend)
    
    Returns:
        The result of a minus b
    """
    return a - b


if __name__ == "__main__":
    # Test the function
    result = subtract_numbers(10, 3)
    print(f"10 - 3 = {result}")
    
    result = subtract_numbers(20, 5)
    print(f"20 - 5 = {result}")
    
    result = subtract_numbers(5, 10)
    print(f"5 - 10 = {result}")
    
    result = subtract_numbers(-5, 3)
    print(f"-5 - 3 = {result}")
    
    result = subtract_numbers(15, -5)
    print(f"15 - (-5) = {result}")
