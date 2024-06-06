# Розробіть простий текстовий інтерфейс для взаємодії з
# користувачем. Користувач повинен мати змогу вибирати дії,
# такі як створення сайту, додавання/видалення сторінок,
# перегляд інформації про сайт
def create_website():
    name = input("Enter website name: ")
    url = input("Enter website URL: ")
    website = create_website(name, url)
    return website

def add_page(website):
    title = input("Enter page title: ")
    content = input("Enter page content: ")
    website.add_page(title, content)

def remove_page(website):
    title = input("Enter title of the page to remove: ")
    website.remove_page(title)

def display_info(website):
    website.display_info()

def main():
    website = None

    while True:
        print("\nMenu:")
        print("1. Create Website")
        print("2. Add Page")
        print("3. Remove Page")
        print("4. Display Website Info")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            website = create_website()
        elif choice == '2':
            if website:
                add_page(website)
            else:
                print("Please create a website first.")
        elif choice == '3':
            if website:
                remove_page(website)
            else:
                print("Please create a website first.")
        elif choice == '4':
            if website:
                display_info(website)
            else:
                print("Please create a website first.")
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

