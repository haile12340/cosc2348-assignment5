#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!

def test_addition():
        result = subprocess.run(["./calculator", "2", "+", "3"], capture_output>
        assert "5" in result.stdout

def test_multiplication():
        result = subprocess.run(["./calculator", "4", "*", "5"], capture_output>
        assert "20" in result.stdout


###

print("All tests passed!")
