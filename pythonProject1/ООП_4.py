class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class Page:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class Website:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.pages = []

    def add_page(self, title, content):
        page = Page(title, content)
        self.pages.append(page)

    def remove_page(self, title):
        for page in self.pages:
            if page.title == title:
                self.pages.remove(page)
                break

    def search_pages(self, keyword):
        found_pages = []
        for page in self.pages:
            if keyword in page.title or keyword in page.content:
                found_pages.append(page)
        return found_pages
website = Website("My Website", "http://example.com")
website.add_page("About Us", "Welcome to our website!")
website.add_page("Contact", "You can reach us at contact@example.com")
results = website.search_pages("Contact")
for page in results:
    print("Title:", page.title)
    print("Content:", page.content)
