# Напишіть програму, яка
# створює словник, де ключами є слова, а значеннями - їхні
# визначення. Дозвольте користувачу додавати, видаляти
# та шукати слова у цьому словнику
dictionary = {}

while True:
    print("\nМеню:")
    print("1. Додати слово та його визначення")
    print("2. Видалити слово")
    print("3. Знайти визначення слова")
    print("4. Вийти з програми")
    choice = input("Виберіть опцію: ")

    if choice == '1':
        word = input("Введіть слово: ")
        definition = input("Введіть визначення: ")
        dictionary[word] = definition
        print(f"Слово '{word}' та його визначення додано до словника.")
    elif choice == '2':
        word = input("Введіть слово, яке потрібно видалити: ")
        if word in dictionary:
            del dictionary[word]
            print(f"Слово '{word}' видалено зі словника.")
        else:
            print("Такого слова немає у словнику.")
    elif choice == '3':
        word = input("Введіть слово для пошуку: ")
        if word in dictionary:
            print(f"Визначення слова '{word}': {dictionary[word]}")
        else:
            print("Такого слова немає у словнику.")
    elif choice == '4':
        print("Програма завершена.")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
