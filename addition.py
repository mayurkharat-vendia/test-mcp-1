def add_numbers(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    return a + b


if __name__ == "__main__":
    # Test the function
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")
    
    result = add_numbers(10, 20)
    print(f"10 + 20 = {result}")
    
    result = add_numbers(-5, 15)
    print(f"-5 + 15 = {result}")
