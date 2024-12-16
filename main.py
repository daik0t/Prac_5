"""Функции 4, 7 и 9(напарник)"""
from math import factorial

def sh(x, iter = 1000):
    result = 0
    for i in range(1, iter):
        result += (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return result

print(sh(100))