# Проверка на четность/нечетность
def check_even_odd():
    number = int(input("Введите целое число: "))
    if number % 2 == 0:
        print("Число", number, "четное.")
    else:
        print("Число", number, "нечетное.")