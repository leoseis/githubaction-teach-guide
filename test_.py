from app import greet, add_numbers


def test_greet():
    assert greet("Ada") == "Hello, Ada!"


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_add_zero():
    assert add_numbers(10, 0) == 10