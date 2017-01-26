class Book:

    ''' Represents one book in a user's list of books'''

    NO_ID = -1
    rating = 'no rating'

    def __init__(self, title, author, read=False, id=NO_ID, rating=rating):
        '''Default book is unread, and has no ID'''
        self.title = title
        self.author = author
        self.read = read
        self.id=id
        self.rating = rating


    def set_id(self, id):
        self.id = id


    def __str__(self):
        read_str = 'no'
        if self.read:
            read_str = 'yes'

        id_str = self.id
        if id == -1:
            id_str = '(no id)'

        template = 'Author: {} id: {} Title: {} Read: {} Rate: {}'
        return template.format(self.author, id_str, self.title, read_str, self.rating)


    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.read == other.read and self.id==other.id and self.rating == other.rating
