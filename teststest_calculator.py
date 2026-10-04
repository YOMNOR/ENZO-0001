# tests/test_calculator.py
from tools.calculator import calculate_expression

def test_addition():
    r = calculate_expression("2 + 3")
    assert r["ok"] and r["result"] == 5

def test_multiplication():
    r = calculate_expression("25 * 48")
    assert r["ok"] and r["result"] == 1200

def test_invalid_chars():
    r = calculate_expression("__import__('os').system('ls')")
    assert not r["ok"]
