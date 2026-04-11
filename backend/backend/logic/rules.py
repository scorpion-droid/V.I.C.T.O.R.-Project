def check_sign(steps):
    """
    Detects if the student incorrectly adds/subtracts and gets the wrong sign
    Example: 
    2x + 3 = 7 → 2x = 10 (wrong)
    """
    if "2x + 3 = 7" in steps and "2x = 10" in steps:
        return "sign error"
    return None

def check_division(steps):
    """
    Detects if student incorrectly divides both sides
    Example:
    2x = 4 → x = 3 (wrong)
    """  
    if "2x = 4" in steps and "x = 3" in steps:
        return "Division Error"
    return None

def detect_error(steps): 
    rules = [
        check_division,
        check_sign
    ]
    for rule in rules: 
        result = rule(steps)
        return result 
    return "All Good"