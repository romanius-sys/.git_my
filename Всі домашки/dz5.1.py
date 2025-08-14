import string
import keyword

name = input("Введіть ім'я змінної: ")

# 1. Не починається з цифри
if name[0].isdigit():
    print(False)
else:
    # 2. Не містить великих літер
    if any(ch.isupper() for ch in name):
        print(False)
    else:
        # 3. Не містить пробілів і знаків пунктуації, крім "_"
        allowed_chars = set(string.ascii_lowercase + string.digits + "_")
        if any(ch not in allowed_chars for ch in name):
            print(False)
        else:
            # 4. Не більше одного підкреслення в усьому імені
            if name.count("_") > 1:
                print(False)
            else:
                # 5. Не входить до списку зареєстрованих слів
                if name in keyword.kwlist:
                    print(False)
                else:
                    print(True)
