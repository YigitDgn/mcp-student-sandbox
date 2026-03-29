from typing import List

MULTIPLIER = 1.15
LOG_FILE = "log.txt"

def apply_multiplier(value: float) -> float:
    """Apply multiplier to a single value."""
    return value * MULTIPLIER

def format_result(value: float) -> str:
    """Format a single value as a string."""
    return f"Total: {value:.2f}"

def log_results(results: List[float]) -> None:
    """Append results to log file."""
    with open(LOG_FILE, "a") as f:
        f.write(str(results) + "\n")

def process_data(data: List[float]) -> List[float]:
    """
    Process data by applying multiplier and logging results.
    
    Args:
        data: List of numeric values to process
        
    Returns:
        List of processed values
    """
    results = [apply_multiplier(value) for value in data]
    
    for result in results:
        formatted = format_result(result)
        print(formatted)
    
    log_results(results)
    return results
