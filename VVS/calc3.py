def calculator():
    print("Калькулятор (операции: + - * / // % **), q - выход")
    while True:
        text = input("\nПервое число (или q): ")
        if text.lower() == "q":
            break
        op = input("Операция: ")
        text2 = input("Второе число: ")

        try:
            a, b = float(text), float(text2)
        except ValueError:
            print("Ошибка: нужно вводить числа")
            continue

        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/" and b != 0:
            result = a / b
        elif op == "//" and b != 0:
            result = a // b
        elif op == "%" and b != 0:
            result = a % b
        elif op == "**":
            result = a ** b
        elif op in ("/", "//", "%"):
            print("Ошибка: деление на ноль")
            continue
        else:
            print("Ошибка: неизвестная операция")
            continue

        print("Результат:", result)

    print("Пока!")


calculator()