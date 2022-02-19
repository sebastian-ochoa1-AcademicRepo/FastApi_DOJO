from db.data import book_data
from models.book_entity import BookEntity, BookEntityUpdate

books = book_data.get('books')

def get_all_books():
    return books


def get_book_by_isbn(isbn:str):
    for book in books:
        if book.get("isbn") == isbn:
            return book
    return None


def create_book(book: BookEntity):
    books.append(book.dict())
    return book


def update_book(isbn: str, book: BookEntityUpdate):
    index = books.index(get_book_by_isbn(isbn))
    books[index].update(book.dict(exclude_unset=True))
    return books[index]


def delete_book(isbn: str):
    book = get_book_by_isbn(isbn)
    if not book:
        return None
    books.remove(book)
    return book
