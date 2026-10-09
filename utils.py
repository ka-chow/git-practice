## @brief Сложение двух чисел.
#  @param a Первое число.
#  @param b Второе число.
#  @return Сумма a и b.
def add(a, b):
    return a + b

## @brief Вычитание двух чисел.
#  @param a Уменьшаемое.
#  @param b Вычитаемое.
#  @return Разность a и b.
def sub(a, b):
    return a - b

## @brief Умножение двух чисел.
#  @param a Первый множитель.
#  @param b Второй множитель.
#  @return Произведение a и b.
def mul(a, b):
    return a * b

## @brief Деление двух чисел.
#  @param a Делимое.
#  @param b Делитель.
#  @return Частное a и b.
#  @exception ValueError Если b равно нулю.
def div(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

## @brief Возведение в степень.
#  @param a Основание.
#  @param b Показатель степени.
#  @return a в степени b.
def pow(a, b):
    return a ** b

## @brief Остаток от деления.
#  @param a Делимое.
#  @param b Делитель.
#  @return Остаток от деления a на b.
def mod(a, b):
    return a % b

## @brief Целочисленное деление.
#  @param a Делимое.
#  @param b Делитель.
#  @return Целая часть от деления a на b.
def floor_div(a, b):
    return a // b