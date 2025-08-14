while True:
    try:
        num1 = float(input("Введіть перше число: "))
        op = input("Введіть операцію (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("Помилка: ділення на нуль!")
                result = None
            else:
                result = num1 / num2
        else:
            print("Невідома операція!")
            result = None

        if result is not None:
            print(f"Результат: {result}")

    except ValueError:
        print("Помилка: введіть числові значення!")

    cont = input("Продовжити? (y/yes для так): ").strip().lower()
    if cont not in ("y", "yes"):
        print("Роботу завершено.")
        break
