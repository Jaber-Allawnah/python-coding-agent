# test_fix.py

from pkg.calculator import Calculator


calc = Calculator()
print("3 + 7 * 2 =", calc.evaluate("3 + 7 * 2"))
print("3 * 4 + 5 =", calc.evaluate("3 * 4 + 5"))
print("2 * 3 - 8 / 2 + 5 =", calc.evaluate("2 * 3 - 8 / 2 + 5"))
