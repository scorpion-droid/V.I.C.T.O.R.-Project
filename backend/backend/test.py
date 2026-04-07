from logic.rules import check_sign
from logic.rules import check_division

steps = [
    "x+7 = 42+81",
    "80x = 35",
    "x=7/16"
]
result = check_sign(steps)
print("Detected Mistake: ", result)

steps = [
    "2x + 3 = 7",
    "2x = 4",
    "x = 3"
]

result = check_division(steps)
print("Detected mistake:", result)