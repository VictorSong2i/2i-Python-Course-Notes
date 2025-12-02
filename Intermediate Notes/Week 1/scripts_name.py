import pytest

"""
Test evenMethod
"""

def even_method(num):
    return num % 2 == 0

def test_Even():
    assert even_method(22) == True
    with pytest.raises(AssertionError):
        assert even_method(7) == True

"""
Test reverse_strings
"""
def reverse_string(s):
    return s[::-1]

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

"""
Test Calculator multiply method
"""

class Calculator:
    def multiply(self, a, b):
        return a * b

def test_calculator():
    calc = Calculator()
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(0, 100) == 0

if __name__ == "__main__":
    pytest.main()
