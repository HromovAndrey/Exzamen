#  Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, які містять слово "Python".
def filter_python_strings(strings):
    return [string for string in strings if "Python" in string]
input_strings = input("Введіть список рядків, розділених комами: ").split(',')
input_strings = [s.strip() for s in input_strings]
result = filter_python_strings(input_strings)
print("Рядки, що містять слово 'Python':", result)
