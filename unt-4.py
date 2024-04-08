# Проверка на простоту
def check_prime():
    number = int(input("Введите целое число больше 1: "))
    if number <= 1:
        print("Число должно быть больше 1.")
        return
    is_prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Число", number, "является простым.")
    else:
        print("Число", number, "не является простым.")