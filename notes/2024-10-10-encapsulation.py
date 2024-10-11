class Book:
    def __init__(self, title, author, year=None):
        self._title  = title
        self.author = author
        self.year   = year

        self.sort_name = self.calcutale_sort_name(title)

    def calcutale_sort_name(self, title):
        if title.startswith('A '):
            return title[2:] + ', A'
        if title[:3] == 'An ':
            return title[3:] + ', An'
        if title[:4] == 'The ':
            return title[4:] + ', The'
        return title

    def get_title(self):
        return self._title

    def info(self):
        return self._title + ' by ' + self.author

    def print(self):
        # print(self.info())
        info = self.info()
        print(info)

    def print_details(self):
        print('This book in detail:')
        print('  Title:  ', self._title)
        print('  Sort as:', self.sort_name)
        print('  Author: ', self.author)
        print('  Year:   ', self.year)

    def set_title(self, title):
        self._title = title
        self.sort_name = self.calcutale_sort_name(title)

    @property
    def title(self):
        return self._title

    def __ge__(self, other):
        return self.sort_name >= other.sort_name

    def __gt__(self, other):
        return self.sort_name > other.sort_name

    def __le__(self, other):
        return self.sort_name <= other.sort_name

    def __lt__(self, other):
        return self.sort_name < other.sort_name


book1 = Book('The Magician\'s Nephew', 'CS Lewis')
book2 = Book('The Lion the Witch and the Wardrobe', 'CS Lewis')
book3 = Book('A Horse and His Boy', 'CS Lewis')
book4 = Book('The Voyage of the Dawn Treader', 'CS Lewis')
book5 = Book('Prince Caspian', 'CS Lewis')
book6 = Book('The Silver Chair', 'CS Lewis')
book7 = Book('The Last Battle', 'CS Lewis')


# book2.print_details()
# book3.print_details()
# book5.print_details()

print('book2.title', book2.get_title())

# Don't mess with _attributes like this!
# book4._title = 'Asdkjavdslfadsladsj'

book7.set_title('Book Seven')
book7.print()

print(book1 >  book2)
print(book2 <= book2)

books = [
    book1,
    book2,
    book3,
    book4,
    book5,
    book6,
    book7,
]

print('==== SORTED =========')
books.sort()
for book in books:
    print(book.info())

# # Using the @property title function:
# print(book1.title)
# # Not allowed on a regular @property:
# book1.title = 'skdhfksdfhjksdjh'
