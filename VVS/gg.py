def levelchoice(l):
    if l == 1:
        test = "пРиВет МИР"

        print("\nДобро пожаловать на первый уровень!")
        print("Данный уровень реализует три метода:")
        print("1) upper() — переводит строку в верхний регистр.")
        print("2) lower() — переводит строку в нижний регистр.")
        print("3) capitalize() — делает первую букву заглавной, остальные строчными.")

        print(
            "Тесты тут!"
            f"\nТестовая строка: {test}"
            f"\n1) {test.upper()}"
            f"\n2) {test.lower()}"
            f"\n3) {test.capitalize()}"
        )

        print("\nВведите строку и номер метода через ', '.")
        print("Например: Привет мир, 1")
        text = input().rsplit(", ", 1)

        if len(text) != 2:
            print("Ошибка: нужно ввести строку и номер метода через ', '.")
            return

        if text[1] == "1":
            print(f"Вывод: {text[0].upper()}")
        elif text[1] == "2":
            print(f"Вывод: {text[0].lower()}")
        elif text[1] == "3":
            print(f"Вывод: {text[0].capitalize()}")
        else:
            print("Такого метода нет.")

    elif l == 2:
        test = "Очень круто"

        print("\nДобро пожаловать на второй уровень!")
        print("Данный уровень реализует три метода:")
        print("1) find() — возвращает индекс первого вхождения подстроки.")
        print("   Если подстрока не найдена, возвращает -1.")
        print("2) replace() — заменяет все вхождения одной подстроки на другую.")
        print("3) count() — считает непересекающиеся вхождения подстроки.")

        print(
            "Тесты тут!"
            f"\nТестовая строка: {test}"
            f"\n1) Найти 'круто': {test.find('круто')}"
            f"\n2) Заменить 'круто' на 'п': {test.replace('круто', 'п')}"
            f"\n3) Посчитать буквы 'о': {test.count('о')}"
        )

        print("\nВведите аргументы через '; '.")
        print("Для поиска: строка; найти; подстрока")
        print("Для замены: строка; заменить; старая подстрока; новая подстрока")
        print("Для подсчёта: строка; посчитать; подстрока")
        text = input().split("; ")

        if len(text) < 3:
            print("Ошибка: недостаточно аргументов.")
            return

        if text[1] == "найти":
            print(f"Вывод: {text[0].find(text[2])}")

        elif text[1] == "заменить":
            if len(text) != 4:
                print("Ошибка: для замены нужны старая и новая подстроки.")
                return

            print(f"Вывод: {text[0].replace(text[2], text[3])}")

        elif text[1] == "посчитать":
            print(f"Вывод: {text[0].count(text[2])}")

        else:
            print("Такого метода нет.")

    elif l == 3:
        test = "Я изучаю Python"
        words = ["Я", "изучаю", "Python"]

        print("\nДобро пожаловать на третий уровень!")
        print("Данный уровень реализует два метода:")
        print("1) split() — разбивает строку на список частей.")
        print("2) join() — объединяет строки из списка через заданный разделитель.")

        print(
            "Тесты тут!"
            f"\nТестовая строка: {test}"
            f"\n1) split(): {test.split()}"
            f"\nТестовый список: {words}"
            f"\n2) join() с разделителем '-': {'-'.join(words)}"
        )

        method = input("\nВведите номер метода (1–2): ").strip()

        if method == "1":
            text = input("Введите строку: ")
            separator = input(
                "Введите разделитель "
                "(Enter — разделение по пробельным символам): "
            )

            if separator == "":
                result = text.split()
            else:
                result = text.split(separator)

            print(f"Вывод: {result}")

        elif method == "2":
            print("Введите элементы списка через '; '.")
            print("Например: Я; изучаю; Python")
            words = input().split("; ")

            separator = input(
                "Введите разделитель для объединения "
                "(Enter — без разделителя): "
            )

            print(f"Вывод: {separator.join(words)}")

        else:
            print("Такого метода нет.")

    elif l == 4:
        digit_test = "12345"
        alpha_test = "Привет"
        strip_test = "   Привет мир   "
        format_test = "Привет, {}! Тебе {} лет."

        print("\nДобро пожаловать на четвёртый уровень!")
        print("Данный уровень реализует четыре метода:")
        print("1) isdigit() — проверяет, состоит ли непустая строка из цифр.")
        print("2) isalpha() — проверяет, состоит ли непустая строка из букв.")
        print("3) strip() — удаляет символы с начала и конца строки.")
        print("   Без аргумента удаляет пробельные символы.")
        print("4) format() — подставляет значения в шаблон строки.")

        print(
            "Тесты тут!"
            f"\n1) {digit_test!r}.isdigit(): {digit_test.isdigit()}"
            f"\n2) {alpha_test!r}.isalpha(): {alpha_test.isalpha()}"
            f"\n3) {strip_test!r}.strip(): {strip_test.strip()!r}"
            f"\n4) format(): {format_test.format('Мир', 20)}"
        )

        method = input("\nВведите номер метода (1–4): ").strip()

        if method == "1":
            text = input("Введите строку: ")
            print(f"Вывод: {text.isdigit()}")

        elif method == "2":
            text = input("Введите строку: ")
            print(f"Вывод: {text.isalpha()}")

        elif method == "3":
            text = input("Введите строку: ")
            chars = input(
                "Введите символы для удаления с краёв "
                "(Enter — пробельные символы): "
            )

            if chars == "":
                result = text.strip()
            else:
                result = text.strip(chars)

            print(f"Вывод: {result!r}")

        elif method == "4":
            print("Введите шаблон с {} или числовыми полями {0}, {1} и т. д.")
            print("Например: Привет, {}! Тебе {} лет.")
            template = input("Шаблон: ")

            print("Введите значения через '; '.")
            print("Например: Мир; 20")
            values = input().split("; ")

            try:
                result = template.format(*values)
                print(f"Вывод: {result}")

            except (IndexError, KeyError, ValueError) as error:
                print(f"Ошибка форматирования: {error}")
                print("Проверьте шаблон и количество введённых значений.")

        else:
            print("Такого метода нет.")

    elif l == 5:
        print("\nДобро пожаловать на пятый уровень!")
        print("На этом уровне программа приводит строку в нормальный вид:")
        print("1) Убирает лишние символы, например @, #, *.")
        print("2) Сохраняет буквы, цифры и знаки . , ! ? : ; -")
        print("3) Убирает лишние пробелы.")
        print("4) Убирает пробелы перед знаками . , ! ? : ;")
        print("5) Убирает одинаковые знаки препинания, стоящие подряд.")
        print("6) Делает первую букву заглавной, остальные строчными.")

        test = "  ***пРИВЕТ   ,,,   мИР!!!###  "

        print(
            "Тесты тут!"
            f"\nТестовая строка: {test!r}"
            f"\nРезультат: {normalize_text(test)!r}"
        )

        text = input("\nВведите строку для обработки: ")
        print(f"Вывод: {normalize_text(text)}")

    else:
        print("Такого уровня нет. Выберите число от 1 до 5.")


def normalize_text(text):
    cleaned = ""

    for char in text:
        if char.isalnum() or char.isspace() or char in ".,!?:;-":
            cleaned += char
        else:
            cleaned += " "

    cleaned = " ".join(cleaned.split())

    for symbol in ".,!?:;":
        cleaned = cleaned.replace(" " + symbol, symbol)

    result = ""

    for char in cleaned:
        if char in ".,!?:;" and result.endswith(char):
            continue

        result += char

    return result.strip().capitalize()


print("Здравствуйте! Добро пожаловать в программу работы со строками!")

try:
    level = int(input("Выберите уровень (1–5): "))
    levelchoice(level)
except ValueError:
    print("Ошибка: номер уровня должен быть целым числом.")