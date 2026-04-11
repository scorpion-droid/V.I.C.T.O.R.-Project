def check_sign(steps):
    if "2x + 3 = 7" in steps and "2x = 7 + 3" in steps:
        return "sign error"
    return None

def check_division(steps):
    if "2x = 4" in steps and "x = 3" in steps:
        return "Division Error"
    return None

def check_multiplication(steps):
    if "2(4x) + 3 = 3(2x) + 7" in steps and "8x + 3 = 9x + 7" in steps:
        return "Multiplication Error"
    return None

def check_subtraction(steps): 
    if "8x - 6x + 3 = 7" in steps and "3x + 3 = 7" in steps:
        return "Subtraction Error"
    return None
    

def detect_error(steps): 
    rules = [
        check_division,
        check_sign,
        check_multiplication,
        check_subtraction
    ]
    
    for rule in rules: 
        result = rule(steps)
        return result 
    return "All Good"