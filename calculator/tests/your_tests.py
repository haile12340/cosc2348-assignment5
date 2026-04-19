	#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!

def test_addition():
        result = run(["./calculator", "2", "+", "3"])
        assert "5" in result.stdout

def test_multiplication():
        result = run(["./calculator", "4", "*", "5"])
        assert "20" in result.stdout


###

print("All tests passed!")
