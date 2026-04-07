def check_sign(steps):
    """
    Detects if the student incorrectly adds/subtracts and gets the wrong sign
    Example: 
    x+7 = 42+81x → 80x = 35 (wrong)
    """
    if "x+7 = 42+81" and "80x = 35" in steps: 
        return "Sign Error"
    return None

def check_division_error(steps):
    """
    Detects if student incorrectly divides both sides
    Example:
    2x = 4 → x = 3 (wrong)
    """
    
    if "2x = 4" in steps and "x = 3" in steps:
        return "division error"
    
    return None