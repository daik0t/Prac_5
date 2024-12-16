"""Функции 4, 7 и 9(напарник)"""
from math import factorial
from decimal import Decimal

def sh(x, iter = 1000):
    result = 0
    for i in range(1, iter):
        result += (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return result

def ln(x, iter = 1000):
    if x > 1 or x <= -1:
        print("x Должен быть от -1 до 1")
        return
    result = 0
    for i in range(1, iter):
        result -= (x ** i) / i
    return result

def last(x, m, iter = 1000):
    pass

while True:
    option = input("1) sh(x), (-∞ < x < +∞)\n\
2) ln(1 - x), (-1 < x <= 1)\n\
3) (1 + x)^m, (-1 < x < 1)\n\
Введите номер функции: ")
    if option not in ["1", "2", "3"]:
        print("Введите номер существующей функции")
        continue
    try:
        x = Decimal(input("Введите x: "))
    except ValueError:
        print("x Должен быть чиселком")
    else:
        if option == "1":
            print(sh(x))
        if option == "2":
            t = ln(x)
            if t != None:
                print(t)
        if option == "3":
            try:
                m = int(input("Введите число m"))
            except ValueError:
                print("m Должно быть числеком")
                continue
            else:
                last(x, m)
    if input("Продолжить? y/n\n") != "y":
        print("Пока")
        break