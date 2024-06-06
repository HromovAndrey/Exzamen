# Розробіть простий текстовий інтерфейс для взаємодії з
# користувачем. Користувач повинен мати змогу вибирати дії,
# такі як створення сайту, додавання/видалення сторінок,
# перегляд інформації про сайт

class Website:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.pages = []

    def add_page(self, title, content):
        self.pages.append({"title": title, "content": content})

    def remove_page(self, title):
        for page in self.pages:
            if page["title"] == title:
                self.pages.remove(page)
                print("Page '{}' removed successfully.".format(title))
                return
        print("Page '{}' not found.".format(title))

    def display_info(self):
        print("Website Name:", self.name)
        print("Website URL:", self.url)
        print("Pages:")
        for page in self.pages:
            print("Title:", page["title"])
            print("Content:", page["content"])
            print("----")

def create_website():
    name = input("Введіть назву сайту: ")
    url = input("Введіть URL-адресу веб-сайту: ")
    return Website(name, url)

def add_page(website):
    title = input("Введіть назву сторінки: ")
    content = input("Введіть вміст сторінки: ")
    website.add_page(title, content)
    print("Page '{}' added successfully.".format(title))

def remove_page(website):
    title = input("Введіть назву сторінки, яку потрібно видалити: ")
    website.remove_page(title)

def display_info(website):
    website.display_info()

def main():
    website = None

    while True:
        print("\nMenu:")
        print("1. Створити сайт")
        print("2. Додати сторінку")
        print("3. Видалити сторінку")
        print("4. Показати інформацію про веб-сайт")
        print("5. Вихід")

        choice = input("Введіть свій вибір: ")

        if choice == '1':
            website = create_website()
        elif choice == '2':
            if website:
                add_page(website)
            else:
                print("Спочатку створіть веб-сайт.")
        elif choice == '3':
            if website:
                remove_page(website)
            else:
                print("Спочатку створіть веб-сайт.")
        elif choice == '4':
            if website:
                display_info(website)
            else:
                print("Спочатку створіть веб-сайт.")
        elif choice == '5':
            print("Вихід...")
            break
        else:
            print("Невірний вибір. Введіть правильний варіант.")

if __name__ == "__main__":
    main()
