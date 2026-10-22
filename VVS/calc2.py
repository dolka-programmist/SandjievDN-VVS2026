def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b


def floor_divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a // b


def modulo(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a % b


def power(a, b):
    return a ** b


def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Нужно ввести число, попробуйте ещё раз.")


def calculate(a, op, b):
    if op == "+":
        return add(a, b)
    if op == "-":
        return subtract(a, b)
    if op == "*":
        return multiply(a, b)
    if op == "/":
        return divide(a, b)
    if op == "//":
        return floor_divide(a, b)
    if op == "%":
        return modulo(a, b)
    if op == "**":
        return power(a, b)
    return "Ошибка: неизвестная операция"


def main():
    print("Калькулятор (операции: + - * / // % **)")
    a = read_number("Первое число: ")
    op = input("Операция: ")
    b = read_number("Второе число: ")
    print("Результат:", calculate(a, op, b))


main()