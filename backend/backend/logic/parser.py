def normalize_steps(steps):
    cleaned = []

    for step in steps: 
        step = step.replace(" ", "")
        step=step.lower()
        cleaned.append(step)
    return cleaned