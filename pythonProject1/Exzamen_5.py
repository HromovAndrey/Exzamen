# . Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери
# Визначаємо функцію для фільтрації рядків
def filter_uppercase_strings(strings):
   return [string for string in strings if string and string[0].isupper()]
input_strings = input("Введіть список рядків, розділених комами: ").split(',')
input_strings = [s.strip() for s in input_strings]
result = filter_uppercase_strings(input_strings)
print("Рядки, що починаються з великої літери:", result)
