# Таблица умножения
def multiplication_table():
    number = int(input("Введите число для таблицы умножения: "))
    print("Таблица умножения для", number)
    for i in range(1, 11):
        print(number, "x", i, "=", number * i)