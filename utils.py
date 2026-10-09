def add(a, b):
    """
    Сложение двух чисел.

    :param a: Первое число.
    :param b: Второе число.
    :return: Сумма a и b.
    """
    return a + b


def sub(a, b):
    """
    Вычитание двух чисел.

    :param a: Уменьшаемое.
    :param b: Вычитаемое.
    :return: Разность a и b.
    """
    return a - b


def mul(a, b):
    """
    Умножение двух чисел.

    :param a: Первый множитель.
    :param b: Второй множитель.
    :return: Произведение a и b.
    """
    return a * b


def div(a, b):
    """
    Деление двух чисел.

    :param a: Делимое.
    :param b: Делитель.
    :return: Частное a и b.
    :raises ValueError: Если b равно нулю.
    """
    if b == 0:
        raise ValueError("Division by zero")
    return a / b


def pow(a, b):
    """
    Возведение в степень.

    :param a: Основание.
    :param b: Показатель степени.
    :return: a в степени b.
    """
    return a ** b


def mod(a, b):
    """
    Остаток от деления.

    :param a: Делимое.
    :param b: Делитель.
    :return: Остаток от деления a на b.
    """
    return a % b


def floor_div(a, b):
    """
    Целочисленное деление.

    :param a: Делимое.
    :param b: Делитель.
    :return: Целая часть от деления a на b.
    """
    return a // b

def square(a):
    """
    Возведение числа в квадрат.

    :param a: Число.
    :return: Квадрат числа a.
    """
    return a * a