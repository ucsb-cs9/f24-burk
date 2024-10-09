class Book:
    def __init__(self, title, author):
        self.title  = title
        self.author = author

    def info(self):
        return self.title + ' by ' + self.author

    def print(self):
        # print(self.info())
        info = self.info()
        print(info)

book = Book('The Stand', 'Stephen King')

book2 = {
    'title':  'The Count of Monte Cristo',
    'author': 'Alexandre Dumas'
}

book3 = Book('The Magician\'s Nephew', 'CS Lewis')
book4 = Book('The Lion the Witch and the Wardrobe', 'CS Lewis')
book5 = Book('A Horse and His Boy', 'CS Lewis')

# print(book.title)
# print(book.author)

# print(book2['title'])
# print(book2['author'])

# print(type(book))
# print(type(book2))

# # book.print()
# print('My favorite book is ' + book.info() + '.')
# print(book.info())

book3.print()
book4.print()
book5.print()

