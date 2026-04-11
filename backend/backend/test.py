from logic.rules import detect_error

steps = [
    "2x + 3 = 7",
    "2x = 4",
    "x = 3"
]

result = detect_error(steps)
print("Detected mistake:", result)