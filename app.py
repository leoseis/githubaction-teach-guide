def greet(name):
    """Return a greeting for a person's name."""
    return f"Hello, {name}!"


def add_numbers(first, second):
    """Return the sum of two numbers."""
    return first + second


if __name__ == "__main__":
    print(greet("Python student"))
    print("2 + 3 =", add_numbers(2, 3))