# Подсчет гласных и согласных
def count_vowels_consonants():
    string = input("Введите строку: ").lower()
    vowels = 'aeiouаеёиоуыэюя'
    consonants = 'bcdfghjklmnpqrstvwxyzбвгджзйклмнпрстфхцчшщ'
    vowel_count = sum(1 for char in string if char in vowels)
    consonant_count = sum(1 for char in string if char in consonants)
    print("Количество гласных:", vowel_count)
    print("Количество согласных:", consonant_count)