#  Напишіть програму, яка створює список цілих чисел та
# виводить новий список, який містить лише парні числа з
# вихідного списку.
# Створюємо список цілих чисел
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_list = [num for num in original_list if num % 2 == 0]
print(even_list)
