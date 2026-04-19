#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!

def test_addition():
        result = run("2 + 3")
        assert "5" in str(result)

def test_multiplication():
        result = run("4 * 5")
        assert "20" in str(result)


###

print("All tests passed!")
