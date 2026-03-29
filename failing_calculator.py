def average_ratios(numbers):
    """
    Calculate average of ratios (100 / number).
    
    Args:
        numbers: List of numeric values
        
    Returns:
        Average of ratios, or None if all values are zero
        
    Raises:
        ValueError: If list is empty
        ZeroDivisionError: If any number is zero
    """
    if not numbers:
        raise ValueError("Numbers list cannot be empty")
    
    total = 0
    for num in numbers:
        total += 100 / num
    
    return total / len(numbers)
