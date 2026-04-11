from logic.rules import detect_error

steps = [
    "2(4x) + 3 = 3(2x) + 7", 
    "8x + 3 = 9x + 7",
    "8x - 6x + 3 = 7",
    "3x + 3 = 7",
    "2x = 7 + 3",
    "2x = 4",
    "x = 3"
]

result = detect_error(steps)
print("Detected mistake:", result)