# Симулятор роботи сайту
# WebSite: Основний клас, який представляє вебсайт.
# Атрибути: назва сайту, URL, список сторінок.
# Методи: додавання/видалення сторінок, відображення
# інформації про сайт.
# WebPage: Клас, який представляє окрему сторінку на сайті.
# Атрибути: заголовок сторінки, вміст, дата публікації.
# Методи: відображення деталей сторінки.

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

    def add_page(self, page):
        self.pages.append(page)

    def remove_page(self, title):
        self.pages = [page for page in self.pages if page.title != title]

    def display_info(self):
        print(f"Website Name: {self.name}")
        print(f"Website URL: {self.url}")
        print("Pages:")
        for page in self.pages:
            print(f" - {page.title}")
page1 = WebPage("Home", "Welcome to our website!")
page2 = WebPage("About", "Learn more about us.")
page3 = WebPage("Contact", "Contact us for more information.")
website = WebSite("MyWebsite", "http://www.mywebsite.com")
website.add_page(page1)
website.add_page(page2)
website.add_page(page3)
website.display_info()
website.remove_page("About")
print("\nAfter removing 'About' page:")
website.display_info()
