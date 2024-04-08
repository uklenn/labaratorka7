# Поиск максимума
def find_max():
    numbers = [int(input("Введите число " + str(i+1) + ": ")) for i in range(3)]
    max_number = max(numbers)
    print("Максимальное число:", max_number)