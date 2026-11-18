"""Small arithmetic helpers used to give the CI pipeline something to test."""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def divide(a, b):
    """Return a divided by b. Raise ValueError when b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
