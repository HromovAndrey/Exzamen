# Реалізація функціональності:
# Дозвольте користувачеві створювати новий сайт з
# певною назвою та URL. Додайте можливість створювати нові
# сторінки для сайту, вводячи заголовок та вміст. Реалізуйте
# функцію для видалення сторінок з сайту. Включіть функцію
# для відображення всієї інформації про сайт, включаючи
# список усіх сторінок.
class WebPage:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Content: {self.content}")


class WebSite:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.pages = []

    def add_page(self, title, content):
        page = WebPage(title, content)
        self.pages.append(page)

    def remove_page(self, title):
        for page in self.pages:
            if page.title == title:
                self.pages.remove(page)
                break

    def display_info(self):
        print(f"Website Name: {self.name}")
        print(f"Website URL: {self.url}")
        print("Pages:")
        for page in self.pages:
            print(f" - {page.title}")
name = input("Enter website name: ")
url = input("Enter website URL: ")
website = WebSite(name, url)
while True:
    choice = input("Do you want to add a new page? (yes/no): ").lower()
    if choice != 'yes':
        break
    title = input("Enter page title: ")
    content = input("Enter page content: ")
    website.add_page(title, content)
while True:
    choice = input("Do you want to remove a page? (yes/no): ").lower()
    if choice != 'yes':
        break
    title = input("Enter title of the page to remove: ")
    website.remove_page(title)

website.display_info()
