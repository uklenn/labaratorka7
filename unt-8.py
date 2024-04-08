# Сумма элементов списка
def sum_of_list():
    numbers = [int(x) for x in input("Введите числа через пробел: ").split()]
    total = sum(numbers)
    print("Сумма элементов списка:", total)