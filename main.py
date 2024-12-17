"""Функции 4, 7 и 9(напарник)"""
from math import factorial
from decimal import Decimal

def sh(x, iter = 1000) -> Decimal:
    """
    Вычисляет значение sh(x) с помощью ряда Маклорена
    
    Parametrs:
        x (Decimlal) : Значение x
        iter (int) : Значение итераций по умолчанию 1000
        
    Returns:
        result (Decimal) : Результат, sh(x)
    
    Raises: 
        None
    
    Example:
        sh(145) = 4.695370643323848906577025200E+62
    """
    result = 0
    for i in range(0, iter):
        result += (x ** (2 * i + 1)) / factorial(2 * i + 1)
    return result

def ln(x, iter = 1000) -> Decimal:
    """
    Вычисляет значение ln(1 - x) с помощью ряда Маклорена
    
    Parametrs:
        x (Decimlal) : Значение x
        iter (int) : Значение итераций по умолчанию 1000
        
    Returns:
        result (Decimal) : Результат, ln(1 - x)
    
    Raises: 
        None
    
    Example:
        ln(1 - 0.1547) = -0.1680636850472550685946214605
    """
    if x > 1 or x <= -1:
        print("x Должен быть от -1 до 1")
        return
    result = 0
    for i in range(1, iter):
        result -= (x ** i) / i
    return result

def last(x, m, iter = 1000):
    """
    Вычисляет значение (1 + x)^m с помощью ряда Маклорена

    Parametrs:
        x (Decimal): Значение x
        iter (int): Значение итераций по умолчанию 1000
        m (Decimal): Значение m

    Returns:
        summ (Decimal): Результат, (1 + x)^m

    Raises:
        None

    Example:
        (1 + 0.99)^99 = 3.858820389035114583782003580E+29
    """
    if x > 1 or x < -1:
        print("x Должен быть от -1 до 1")
        return
    summ = 1
    k = 1
    for i in range (-1, iter):
        k = k*(m-(i+1))
        summ = summ + (k/factorial(i+2))*(x**(i+2))
    return summ

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
                print(last(x, Decimal(m)))
    if input("Продолжить? y/n\n") != "y":
        print("Пока")
        break
