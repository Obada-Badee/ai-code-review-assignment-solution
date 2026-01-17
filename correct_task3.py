# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
def average_valid_measurements(values):
    total = 0
    count = 0

    for v in values:
        if v is not None:
            try:
                total += float(v)
                count += 1
            except (ValueError, TypeError):
                pass  # Skip invalid values

    if count > 0:
        return total / count
    else:
        return 0
