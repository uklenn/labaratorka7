# Палиндром
def is_palindrome():
    string = input("Введите строку: ").lower().replace(" ", "")
    if string == string[::-1]:
        print("Строка является палиндромом.")
    else:
        print("Строка не является палиндромом.")