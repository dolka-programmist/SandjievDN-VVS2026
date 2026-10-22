class Calculator:
    OPERATIONS = ("+", "-", "*", "/", "//", "%", "**")

    def __init__(self):
        self.history = []
        self.last_result = None

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("деление на ноль")
        return a / b

    def floor_divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("деление на ноль")
        return a // b

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("деление на ноль")
        return a % b

    def power(self, a, b):
        return a ** b

    def calculate(self, a, op, b):
        methods = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide,
            "//": self.floor_divide,
            "%": self.modulo,
            "**": self.power,
        }
        if op not in methods:
            raise ValueError("неизвестная операция")
        result = methods[op](a, b)
        self.last_result = result
        self.history.append(f"{a} {op} {b} = {result}")
        return result

    def show_history(self):
        if not self.history:
            print("История пуста.")
        for i, line in enumerate(self.history, 1):
            print(f"{i}. {line}")

    def run(self):
        print("Калькулятор (операции: + - * / // % **)")
        print("Команды: h - история, q - выход")
        while True:
            text = input("\nПервое число: ").strip().lower()
            if text == "q":
                break
            if text == "h":
                self.show_history()
                continue
            op = input("Операция: ").strip()
            try:
                a = float(text)
                b = float(input("Второе число: "))
                print("Результат:", self.calculate(a, op, b))
            except ValueError as e:
                print("Ошибка:", e if "операция" in str(e) else "нужно вводить числа")
            except ZeroDivisionError as e:
                print("Ошибка:", e)


if __name__ == "__main__":
    Calculator().run()